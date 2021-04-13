﻿"""
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

import secrets

import discord

from sigma.core.utilities.data_processing import user_avatar

rarity_rewards = {
    '🍆': 0.525,
    '🍒': 0.55,
    '⚓': 0.575,
    '🏵': 0.6,
    '💖': 0.625,
    '🏮': 0.65,
    '🍥': 0.675,
    '💵': 0.7,
    '💳': 0.725,
    '🎁': 0.75,
    '🐬': 0.775,
    '🐦': 0.8,
    '🌟': 0.825,
    '🦊': 0.85,
    '🦋': 0.875,
    '🐍': 0.9,
    '🍬': 0.925,
    '💎': 0.95,
    '🔰': 0.975,
    '⚜': 1
}

symbols = []
for symbol in rarity_rewards:
    symbols.append(symbol)

TWO_MOD = int(len(symbols) / 2)
THREE_MOD = len(symbols) ** 2


async def slots(cmd, pld):
    """
    :param cmd: The command object referenced in the command.
    :type cmd: sigma.core.mechanics.command.SigmaCommand
    :param pld: The payload with execution data and details.
    :type pld: sigma.core.mechanics.payload.CommandPayload
    """
    currency_icon = cmd.bot.cfg.pref.currency_icon
    currency = cmd.bot.cfg.pref.currency
    current_kud = await cmd.db.get_resource(pld.msg.author.id, 'currency')
    current_kud = current_kud.current
    if pld.args:
        try:
            bet = abs(int(pld.args[0]))
        except ValueError:
            bet = 10
    else:
        bet = 10
    if current_kud >= bet:
        if not await cmd.bot.cool_down.on_cooldown(cmd.name, pld.msg.author):
            base_cooldown = 60
            cooldown = int(base_cooldown - ((base_cooldown / 100) * ((0 * 0.5) / (1.25 + (0.01 * 0)))))
            cooldown = 5 if cooldown < 5 else cooldown
            await cmd.bot.cool_down.set_cooldown(cmd.name, pld.msg.author, cooldown)
            await cmd.db.del_resource(pld.msg.author.id, 'currency', bet, cmd.name, pld.msg)
            out_list = []
            for x in range(0, 3):
                temp_list = []
                for y in range(0, 3):
                    symbol_choice = secrets.choice(symbols)
                    temp_list.append(symbol_choice)
                out_list.append(temp_list)
            slot_lines = f'⏸{"".join(out_list[0])}⏸'
            slot_lines += f'\n▶{"".join(out_list[1])}◀'
            slot_lines += f'\n⏸{"".join(out_list[2])}⏸'
            combination = out_list[1]
            three_comb = bool(combination[0] == combination[1] == combination[2])
            two_comb_one = bool(combination[0] == combination[1])
            two_comb_two = bool(combination[0] == combination[2])
            two_comb_three = bool(combination[1] == combination[2])
            if three_comb:
                win = True
                winnings = int(bet * rarity_rewards[combination[0]] * THREE_MOD * 0.95)
            elif two_comb_one or two_comb_two or two_comb_three:
                if combination[0] == combination[1]:
                    win_comb = combination[0]
                elif combination[0] == combination[2]:
                    win_comb = combination[0]
                elif combination[1] == combination[2]:
                    win_comb = combination[1]
                else:
                    win_comb = None
                win = True
                winnings = int(bet * rarity_rewards[win_comb] * TWO_MOD * 0.9)
            else:
                win = False
                winnings = 0
            if win:
                color = 0x5dadec
                title = '💎 Congrats, you won!'
                footer = f'{currency_icon} {winnings} {currency} has been awarded.'
                await cmd.db.add_resource(pld.msg.author.id, 'currency', winnings, cmd.name, pld.msg, False)
            else:
                color = 0x232323
                title = '💣 Oh my, you lost...'
                footer = f'{currency_icon} {bet} {currency} has been deducted.'
            response = discord.Embed(color=color)
            response.set_author(name=pld.msg.author.display_name, icon_url=user_avatar(pld.msg.author))
            response.add_field(name=title, value=slot_lines)
            response.set_footer(text=footer)
        else:
            timeout = await cmd.bot.cool_down.get_cooldown(cmd.name, pld.msg.author)
            response = discord.Embed(color=0x696969, title=f'🕙 You can spin again in {timeout} seconds.')
    else:
        response = discord.Embed(color=0xa7d28b, title=f'💸 You don\'t have {bet} {currency}.')
    await pld.msg.channel.send(embed=response)
