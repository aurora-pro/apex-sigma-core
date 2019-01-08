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


async def addreactor(cmd: SigmaCommand, pld: CommandPayload):
    if pld.msg.author.permissions_in(pld.msg.channel).manage_guild:
        if pld.args:
            if len(pld.args) == 2:
                trigger = pld.args[0].lower()
                if '.' not in trigger:
                    reaction = pld.args[1].replace('<', '').replace('>', '')
                    react_triggers = pld.settings.get('reactor_triggers', {})
                    res_text = 'updated' if trigger in react_triggers else 'added'
                    react_triggers.update({trigger: reaction})
                    await cmd.db.set_guild_settings(pld.msg.guild.id, 'reactor_triggers', react_triggers)
                    response = discord.Embed(color=0x66CC66, title=f'✅ {trigger} has been {res_text}')
                else:
                    response = discord.Embed(color=0xBE1931, title='❗ The trigger can\'t have a dot in it.')
            else:
                response = discord.Embed(color=0xBE1931, title='❗ Invalid number of arguments.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
    else:
        response = denied('Manage Server')
    await pld.msg.channel.send(embed=response)
