# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2017  Lucia's Cipher
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

from sigma.core.mechanics.event import SigmaEvent


async def remover_detector(ev: SigmaEvent, emoji: discord.PartialEmoji, mid: int, cid: int, uid: int):
    if uid in ev.bot.cfg.dsc.owners:
        log_ch_id = ev.bot.modules.commands.get('addreact').cfg.get('log_ch')
        if cid is not None and cid == log_ch_id:
            if emoji.name == '❌':
                interaction_item = await ev.db[ev.db.db_cfg.database].Interactions.find_one({'MessageID': mid})
                if interaction_item:
                    await ev.db[ev.db.db_cfg.database].Interactions.delete_one(interaction_item)
                    channel = discord.utils.find(lambda c: c.id == cid, ev.bot.get_all_channels())
                    message = await channel.get_message(mid) if channel else None
                    if message:
                        await message.add_reaction('🔥')
