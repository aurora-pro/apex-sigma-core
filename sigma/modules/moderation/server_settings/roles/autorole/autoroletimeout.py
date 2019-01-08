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


async def autoroletimeout(cmd: SigmaCommand, pld: CommandPayload):
    if pld.msg.author.permissions_in(pld.msg.channel).manage_guild:
        if pld.args:
            try:
                timeout = abs(int(pld.args[0]))
            except ValueError:
                timeout = None
            if timeout is not None:
                await cmd.db.set_guild_settings(pld.msg.guild.id, 'auto_role_timeout', timeout)
                response = discord.Embed(color=0x77B255, title=f'✅ Timeout set to {timeout} seconds.')
            else:
                response = discord.Embed(color=0xBE1931, title='❗ This role is above my highest role.')
        else:
            timeout = pld.settings.get('auto_role_timeout', 0)
            response = discord.Embed(color=0x696969, title=f'🕙 The current timeout is {timeout} seconds.')
    else:
        response = denied('Manage Server')
    await pld.msg.channel.send(embed=response)
