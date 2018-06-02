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

import secrets

import arrow
import discord

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.utilities.data_processing import convert_to_seconds, user_avatar

raffle_icons = ['⭐', '💎', '🎉', '🎁', '📥']
icon_colors = {'⭐': 0xffac33, '💎': 0x5dadec, '🎉': 0xdd2e44, '🎁': 0xfdd888, '📥': 0x77b255}


async def raffle(cmd: SigmaCommand, message: discord.Message, args: list):
    if len(args) >= 2:
        time_input = args[0]
        raffle_title = ' '.join(args[1:])
        try:
            time_sec = convert_to_seconds(time_input)
            start_stamp = arrow.utcnow().float_timestamp
            end_stamp = start_stamp + time_sec
            end_dt = arrow.get(end_stamp).datetime
            if time_sec < 90:
                end_hum = f'in {time_sec} seconds'
            else:
                end_hum = arrow.get(end_stamp).humanize()
            rafid = secrets.token_hex(3)
            reaction_icon = secrets.choice(raffle_icons)
            icon_color = icon_colors.get(reaction_icon)
            resp_title = f'{message.author.display_name} started a raffle!'
            starter = discord.Embed(color=icon_color, timestamp=end_dt)
            starter.set_author(name=resp_title, icon_url=user_avatar(message.author))
            starter.description = f'Reward: **{raffle_title}**'
            starter.description += f'\nReact with a {reaction_icon} to enter the raffle.'
            starter.set_footer(text=f'[{rafid}] Raffle ends {end_hum}.')
            starter_message = await message.channel.send(embed=starter)
            await starter_message.add_reaction(reaction_icon)
            raffle_data = {
                'Author': message.author.id,
                'Channel': message.channel.id,
                'Title': raffle_title,
                'Start': start_stamp,
                'End': end_stamp,
                'Icon': reaction_icon,
                'Color': icon_color,
                'Message': starter_message.id,
                'Active': True,
                'ID': rafid
            }
            await cmd.db[cmd.db.db_cfg.database].Raffles.insert_one(raffle_data)
            response = None
        except (LookupError, ValueError):
            response = discord.Embed(color=0xBE1931, title='❗ Please use the format HH:MM:SS.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Nothing inputted.')
    if response:
        await message.channel.send(embed=response)
