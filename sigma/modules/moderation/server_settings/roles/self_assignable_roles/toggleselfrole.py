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
from sigma.core.utilities.generic_responses import permission_denied


async def toggleselfrole(cmd: SigmaCommand, message: discord.Message, args: list):
    if message.author.guild_permissions.manage_roles:
        if args:
            lookup = ' '.join(args)
            target_role = discord.utils.find(lambda x: x.name.lower() == lookup.lower(), message.guild.roles)
            if target_role:
                role_bellow = bool(target_role.position < message.guild.me.top_role.position)
                if role_bellow:
                    selfroles = await cmd.db.get_guild_settings(message.guild.id, 'SelfRoles')
                    if selfroles is None:
                        selfroles = []
                    if target_role.id in selfroles:
                        selfroles.remove(target_role.id)
                        await cmd.db.set_guild_settings(message.guild.id, 'SelfRoles', selfroles)
                        response = discord.Embed(color=0x77B255, title=f'✅ {target_role.name} removed.')
                    else:
                        selfroles.append(target_role.id)
                        await cmd.db.set_guild_settings(message.guild.id, 'SelfRoles', selfroles)
                        response = discord.Embed(color=0x77B255, title=f'✅ {target_role.name} added.')
                else:
                    response = discord.Embed(color=0xBE1931, title='❗ This role is above my highest role.')
            else:
                response = discord.Embed(color=0x696969, title=f'🔍 {lookup} not found.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
    else:
        response = permission_denied('Manage Roles')
    await message.channel.send(embed=response)
