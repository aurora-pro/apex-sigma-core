# Apex Sigma: The Database Giant Discord Bot.
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
from sigma.core.utilities.generic_responses import permission_denied
from sigma.core.utilities.data_processing import user_avatar
from sigma.core.utilities.event_logging import log_event
from sigma.core.utilities.permission_processing import hierarchy_permit


def generate_log_embed(message, target, args):
    log_embed = discord.Embed(color=0x696969, timestamp=arrow.utcnow().datetime)
    log_embed.set_author(name='A Member Has Been Hard Muted', icon_url=user_avatar(target))
    log_embed.add_field(name='🔇 Muted User',
                        value=f'{target.mention}\n{target.name}#{target.discriminator}', inline=True)
    author = message.author
    log_embed.add_field(name='🛡 Responsible',
                        value=f'{author.mention}\n{author.name}#{author.discriminator}', inline=True)
    if len(args) > 1:
        log_embed.add_field(name='📄 Reason', value=f"```\n{' '.join(args[1:])}\n```", inline=False)
    log_embed.set_footer(text=f'UserID: {target.id}')
    return log_embed


async def hardmute(cmd: SigmaCommand, message: discord.Message, args: list):
    if message.author.permissions_in(message.channel).manage_channels:
        if message.mentions:
            target = message.mentions[0]
            if len(args) > 1:
                reason = ' '.join(args[1:])
            else:
                reason = 'Not stated.'
            hierarchy_me = hierarchy_permit(message.guild.me, target)
            if hierarchy_me:
                hierarchy_auth = hierarchy_permit(message.author, target)
                if hierarchy_auth:
                    ongoing = discord.Embed(color=0x696969, title='⛓ Editing permissions...')
                    ongoing_msg = await message.channel.send(embed=ongoing)
                    for channel in message.guild.channels:
                        if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.CategoryChannel):
                            try:
                                await channel.set_permissions(target, send_messages=False, add_reactions=False)
                            except discord.Forbidden:
                                pass
                    await ongoing_msg.delete()
                    log_embed = generate_log_embed(message, target, args)
                    await log_event(cmd.bot, message.guild, cmd.db, log_embed, 'LogMutes')
                    title = f'✅ {target.display_name} has been hard-muted.'
                    response = discord.Embed(color=0x77B255, title=title)
                    to_target_title = f'🔇 You have been hard-muted.'
                    to_target = discord.Embed(color=0x696969)
                    to_target.add_field(name=to_target_title, value=f'Reason: {reason}')
                    to_target.set_footer(text=f'On: {message.guild.name}', icon_url=message.guild.icon_url)
                    try:
                        await target.send(embed=to_target)
                    except discord.Forbidden:
                        pass
                else:
                    response = discord.Embed(color=0xBE1931, title='❗ That user is equal or above you.')
            else:
                response = discord.Embed(color=0xBE1931, title='❗ I can\'t mute a user equal or above me.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ No user targeted.')
    else:
        response = permission_denied('Manage Channels')
    await message.channel.send(embed=response)
