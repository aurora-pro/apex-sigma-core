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

import discord

from sigma.core.mechanics.command import SigmaCommand


async def wfsortiechannel(cmd: SigmaCommand, message: discord.Message, args: list):
    if message.author.permissions_in(message.channel).manage_channels:
        if message.channel_mentions:
            target_channel = message.channel_mentions[0]
        else:
            if args:
                if args[0].lower() == 'disable':
                    await cmd.db.set_guild_settings(message.guild.id, 'WarframeSortieChannel', None)
                    response = discord.Embed(color=0x66CC66, title=f'✅ Warframe Sortie Channel Disabled')
                    await message.channel.send(embed=response)
                    return
                else:
                    return
            else:
                target_channel = message.channel
        await cmd.db.set_guild_settings(message.guild.id, 'WarframeSortieChannel', target_channel.id)
        response = discord.Embed(color=0x66CC66, title=f'✅ Warframe Sortie Channel set to #{target_channel.name}')
    else:
        response = discord.Embed(color=0xBE1931, title='⛔ Access Denied. Manage Channels needed.')
    await message.channel.send(embed=response)
