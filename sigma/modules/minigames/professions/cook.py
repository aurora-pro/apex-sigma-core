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
from sigma.core.utilities.data_processing import user_avatar
from .nodes.item_core import ItemCore
from .nodes.properties import cook_quality
from .nodes.recipe_core import RecipeCore

item_core = None
recipe_core = None


async def cook(cmd: SigmaCommand, message: discord.Message, args: list):
    global item_core
    global recipe_core
    if not item_core:
        item_core = ItemCore(cmd.resource('data'))
    if not recipe_core:
        recipe_core = RecipeCore(cmd.resource('data'))
    if args:
        lookup = ' '.join(args)
        recipe = recipe_core.find_recipe(lookup)
        used_items = []
        if recipe:
            req_satisfied = True
            for ingredient in recipe.ingredients:
                user_inv = await cmd.db.get_inventory(message.author)
                in_inventory = False
                for item in user_inv:
                    if item['item_file_id'] == ingredient.file_id:
                        used_items.append(item)
                        in_inventory = True
                        break
                if not in_inventory:
                    req_satisfied = False
            if req_satisfied:
                cooked_item_data = item_core.get_item_by_name(recipe.name).generate_inventory_item()
                await cmd.db.add_to_inventory(message.author, cooked_item_data)
                await item_core.add_item_statistic(cmd.db, recipe, message.author)
                for req_item in used_items:
                    await cmd.db.del_from_inventory(message.author, req_item['item_id'])
                quality = cook_quality[cooked_item_data['quality']]
                connector = 'a'
                if quality[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                    connector = 'an'
                head_title = f'{recipe.icon} You made {connector} {quality.lower()} {recipe.name}'
                response = discord.Embed(color=recipe.color, title=head_title)
                response.set_author(name=message.author.display_name, icon_url=user_avatar(message.author))
            else:
                response = discord.Embed(color=0xBE1931, title=f'❗ You\'re missing ingredients.')
        else:
            response = discord.Embed(color=0x696969, title=f'🔍 Recipe not found.')
    else:
        response = discord.Embed(color=0xBE1931, title=f'❗ Nothing inputted.')
    await message.channel.send(embed=response)
