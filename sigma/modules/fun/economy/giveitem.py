"""
Apex Sigma: The Database Giant Discord Bot.
Copyright (C) 2019  Lucia's Cipher

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from sigma.core.utilities.generic_responses import GenericResponse
from sigma.modules.minigames.professions.nodes.item_core import get_item_core


async def giveitem(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    item_core = await get_item_core(cmd.db)
    if len(pld.args) > 1:
        if pld.msg.mentions:
            target = pld.msg.mentions[0]
            if not target.bot:
                lookup = ' '.join(pld.args[1:])
                obj_item = item_core.get_item_by_name(lookup)
                if obj_item:
                    inv_item = await cmd.db.get_inventory_item(pld.msg.author.id, obj_item.file_id)
                    if inv_item:
                        inv = await cmd.db.get_inventory(target.id)
                        inv_limit = 128
                        author_sab = await cmd.db.is_sabotaged(pld.msg.author.id)
                        target_sab = await cmd.db.is_sabotaged(target.id)
                        if len(inv) < inv_limit:
                            if not author_sab and not target_sab:
                                await cmd.db.del_from_inventory(pld.msg.author.id, inv_item.get('item_id'))
                                inv_item.update({'transferred': True})
                                await cmd.db.add_to_inventory(target.id, inv_item)
                                await cmd.db.add_resource(target.id, 'items', 1, cmd.name, pld.msg, True)
                                response = GenericResponse(
                                    f'Transferred {obj_item.name} to {target.display_name}.'
                                ).ok()
                                response.set_footer(text=f'Item ID: {inv_item.get("item_id")}')
                            else:
                                response = GenericResponse('Transfer declined by Chamomile.').error()
                        else:
                            response = GenericResponse(f'{target.name}\'s inventory is full.').error()
                    else:
                        response = GenericResponse(f'No {obj_item.name} found in your inventory.').not_found()
                else:
                    response = GenericResponse('No such item exists.').not_found()
            else:
                response = GenericResponse('Can\'t give items to bots.').error()
        else:
            response = GenericResponse('No user targeted.').error()
    else:
        response = GenericResponse('Not enough arguments.').error()
    await pld.msg.channel.send(embed=response)
