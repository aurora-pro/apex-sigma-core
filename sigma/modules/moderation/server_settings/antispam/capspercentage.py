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
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.generic_responses import denied


async def capspercentage(cmd: SigmaCommand, pld: CommandPayload):
    if pld.msg.author.permissions_in(pld.msg.channel).manage_guild:
        limit = None
        if pld.args:
            try:
                limit = abs(int(pld.args[0]))
            except ValueError:
                limit = None
        limit = 100 if limit > 100 else limit
        if limit is not None:
            await cmd.db.set_guild_settings(pld.msg.guild.id, 'caps_percentage', limit)
            response = discord.Embed(color=0x77B255, title=f'✅ Capital letter percentage set to {limit}%.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Missing or invalid limit given.')
    else:
        response = denied('Manage Server')
    await pld.msg.channel.send(embed=response)
