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

import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.permissions import scp_cache
from .nodes.permission_data import get_all_perms


async def enablecommand(cmd: SigmaCommand, message: discord.Message, args: list):
    if args:
        if not message.author.permissions_in(message.channel).manage_guild:
            response = discord.Embed(color=0xBE1931, title='⛔ Access Denied. Manage Server needed.')
        else:
            cmd_name = args[0].lower()
            if cmd_name in cmd.bot.modules.alts:
                cmd_name = cmd.bot.modules.alts[cmd_name]
            if cmd_name in cmd.bot.modules.commands:
                perms = await get_all_perms(cmd.db, message)
                disabled_commands = perms['DisabledCommands']
                if cmd_name in disabled_commands:
                    disabled_commands.remove(cmd_name)
                    perms.update({'DisabledCommands': disabled_commands})
                    await cmd.db[cmd.db.db_cfg.database].Permissions.update_one({'ServerID': message.guild.id},
                                                                                {'$set': perms})
                    scp_cache.del_cache(message.guild.id)
                    response = discord.Embed(color=0x77B255, title=f'✅ `{cmd_name.upper()}` enabled.')
                else:
                    response = discord.Embed(color=0xFFCC4D, title='⚠ Command not disabled')
            else:
                response = discord.Embed(color=0x696969, title='🔍 Command not found.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted')
    await message.channel.send(embed=response)
