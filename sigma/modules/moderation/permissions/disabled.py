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
from sigma.core.mechanics.paginator import PaginatorCore
from sigma.core.mechanics.payload import CommandPayload
from sigma.core.utilities.data_processing import get_image_colors
from sigma.modules.moderation.permissions.nodes.permission_data import get_all_perms


def get_perm_type(cmd: SigmaCommand, perm_type: str):
    if perm_type == 'modules':
        perm_name = 'modules'
        perm_type = 'disabled_modules'
        exception_type = 'module_exceptions'
        item_list = cmd.bot.modules.categories
    elif perm_type == 'commands':
        perm_name = 'commands'
        perm_type = 'disabled_commands'
        exception_type = 'command_exceptions'
        item_list = cmd.bot.modules.commands
    else:
        perm_name, perm_type = None, None
        exception_type, item_list = None, None
    return perm_name, perm_type, exception_type, item_list


async def disabled(cmd: SigmaCommand, pld: CommandPayload):
    message, args = pld.msg, pld.args
    if args:
        perm_name, perm_type, exception_type, item_list = get_perm_type(cmd, args[0].lower())
        if perm_name:
            perms = await get_all_perms(cmd.db, message)
            disabled_items = perms[perm_type]
            overridden_items = perms[exception_type]
            disabled_list = []
            for item_name in disabled_items:
                if item_name in item_list:
                    if item_name in overridden_items:
                        exc = overridden_items.get(item_name)
                        exc_exists = any([exc.get('users'), exc.get('channels'), exc.get('roles')])
                        if exc_exists:
                            item_name += '\*'
                    disabled_list.append(item_name)
            if disabled_list:
                disabled_count = len(disabled_list)
                page = args[1] if len(args) > 1 else 1
                disabled_list, page_num = PaginatorCore.paginate(disabled_list, page, 50)
                title = f'{message.guild.name} Disabled {perm_name.title()}'
                info = f'[Page {page_num}] Showing {len(disabled_list)} out of {disabled_count} disabled {perm_name}.'
                response = discord.Embed(color=await get_image_colors(message.guild.icon_url))
                response.set_author(name=title, icon_url=message.guild.icon_url)
                response.description = ', '.join(disabled_list)
                response.set_footer(text=info)
            else:
                response = discord.Embed(color=0x696969, title=f'🔍 No disabled {perm_name} found.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Invalid permission type.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
    await message.channel.send(embed=response)