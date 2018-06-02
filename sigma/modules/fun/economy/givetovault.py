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


async def givetovault(cmd: SigmaCommand, message: discord.Message, args: list):
    if args:
        try:
            amount = int(abs(int(args[0])))
        except ValueError:
            amount = None
        if amount:
            currency = cmd.bot.cfg.pref.currency
            current_kud = await cmd.db.get_currency(message.author, message.guild)
            current_kud = current_kud.get('current')
            if current_kud >= amount:
                current_vault = await cmd.db.get_guild_settings(message.guild.id, 'CurrencyVault')
                if current_vault is None:
                    current_vault = 0
                await cmd.db.rmv_currency(message.author, amount)
                current_vault += amount
                await cmd.db.set_guild_settings(message.guild.id, 'CurrencyVault', current_vault)
                title_text = f'✅ You added {amount} {currency} to the Vault.'
                response = discord.Embed(color=0x77B255, title=title_text)
            else:
                response = discord.Embed(color=0xa7d28b, title=f'💸 You don\'t have enough {currency}.')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Invalid amount.')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ Amount missing.')
    await message.channel.send(embed=response)
