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

import discord

from sigma.core.mechanics.paginator import PaginatorCore
from sigma.core.utilities.generic_responses import GenericResponse


async def whoplays(_cmd, pld):
    """
    :param _cmd: The command object referenced in the command.
    :type _cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    if pld.args:
        if pld.args[0].isdigit():
            game_title = ' '.join(pld.args[1:])
            page = True
        else:
            game_title = ' '.join(pld.args)
            page = False
        game_name = None
        gamer_list = []
        playing, total = 0, 0
        for member in pld.msg.guild.members:
            if not member.activities:
                continue
            activity = member.activities[-1]
            is_custom = isinstance(activity, discord.CustomActivity)
            is_spotify = isinstance(activity, discord.Spotify)
            if is_custom or is_spotify:
                continue
            total += 1
            if activity.name.lower() == game_title.lower():
                if not game_name:
                    game_name = activity.name
                member_name = member.name
                for escapable in '*_~`':
                    member_name = member_name.replace(escapable, f'\\{escapable}')
                gamer_list.append(member_name)
                playing += 1
        title = f'{playing}/{total} people are playing {game_name}'
        if gamer_list:
            total_gamers = len(gamer_list)
            page = pld.args[0] if page else 1
            gamer_list, page = PaginatorCore.paginate(sorted(gamer_list), page, 20)
            gamers = '- ' + '\n- '.join(gamer_list)
            response = discord.Embed(color=0x1ABC9C)
            response.add_field(name=title, value=gamers)
            response.set_footer(text=f'[Page {page}] Showing {len(gamer_list)} out of {total_gamers} users.')
        else:
            response = GenericResponse(f'No users are currently playing {game_title}.').not_found()
    else:
        response = GenericResponse('Nothing inputted.').error()
    await pld.msg.channel.send(embed=response)
