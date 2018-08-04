﻿# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2018  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import arrow
import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.utilities.data_processing import user_avatar, convert_to_seconds
from sigma.core.utilities.event_logging import log_event
from sigma.core.utilities.generic_responses import permission_denied
from sigma.core.utilities.permission_processing import hierarchy_permit


def generate_log_embed(message, target, reason):
    log_embed = discord.Embed(color=0x696969, timestamp=arrow.utcnow().datetime)
    log_embed.set_author(name='A Member Has Been Muted', icon_url=user_avatar(target))
    log_embed.add_field(name='🔇 Muted User',
                        value=f'{target.mention}\n{target.name}#{target.discriminator}')
    author = message.author
    log_embed.add_field(name='🛡 Responsible',
                        value=f'{author.mention}\n{author.name}#{author.discriminator}')
    if reason:
        log_embed.add_field(name='📄 Reason', value=f"```\n{reason}\n```", inline=False)
    log_embed.set_footer(text=f'user_id: {target.id}')
    return log_embed


async def textmute(cmd: SigmaCommand, message: discord.Message, args: list):
    if not message.author.permissions_in(message.channel).manage_messages:
        response = permission_denied('Manage Messages')
    else:
        if not message.mentions:
            response = discord.Embed(color=0xBE1931, title='❗ No user targeted.')
        else:
            author = message.author
            target = message.mentions[0]
            if author.id == target.id:
                response = discord.Embed(color=0xBE1931, title='❗ Can\'t mute yourself.')
            else:
                above_hier = hierarchy_permit(author, target)
                if not above_hier:
                    response = discord.Embed(color=0xBE1931, title='⛔ Can\'t mute someone equal or above you.')
                else:
                    timed = args[-1].startswith('--time=')
                    endstamp = arrow.utcnow().timestamp + convert_to_seconds(args[-1].split('=')[-1]) if timed else None
                    mute_list = await cmd.db.get_guild_settings(message.guild.id, 'MutedUsers')
                    if mute_list is None:
                        mute_list = []
                    if target.id in mute_list:
                        resp_title = f'❗ {target.display_name} is already text muted.'
                        response = discord.Embed(color=0xBE1931, title=resp_title)
                    else:
                        mute_list.append(target.id)
                        await cmd.db.set_guild_settings(message.guild.id, 'MutedUsers', mute_list)
                        response = discord.Embed(color=0x77B255, title=f'✅ {target.display_name} has been text muted.')
                        rarg = args[1:-1] if timed else args[1:] if args[1:] else None
                        reason = ' '.join(rarg) if rarg else None
                        log_embed = generate_log_embed(message, target, reason)
                        await log_event(cmd.bot, message.guild, cmd.db, log_embed, 'LogMutes')
                        to_target_title = f'🔇 You have been text muted.'
                        to_target = discord.Embed(color=0x696969)
                        to_target.add_field(name=to_target_title, value=f'Reason: {reason}')
                        to_target.set_footer(text=f'On: {message.guild.name}', icon_url=message.guild.icon_url)
                        try:
                            await target.send(embed=to_target)
                        except discord.Forbidden:
                            pass
                        if endstamp:
                            doc_data = {'server_id': message.guild.id, 'user_id': target.id, 'Time': endstamp}
                            await cmd.db[cmd.db.db_nam].TextmuteClockworkDocs.insert_one(doc_data)
    await message.channel.send(embed=response)
