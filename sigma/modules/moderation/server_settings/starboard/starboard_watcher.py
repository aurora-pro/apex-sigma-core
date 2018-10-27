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

import arrow
import discord

from sigma.core.mechanics.database import Database
from sigma.core.mechanics.event import SigmaEvent
from sigma.core.mechanics.payload import RawReactionPayload
from sigma.core.utilities.data_processing import user_avatar, get_image_colors


async def post_starboard(msg: discord.Message, response: discord.Embed, sbc: int):
    channel = msg.guild.get_channel(sbc)
    if channel:
        try:
            await channel.send(embed=response)
        except Exception:
            pass


async def generate_embed(msg: discord.Message):
    avatar = user_avatar(msg.author)
    user_color = await get_image_colors(avatar)
    response = discord.Embed(color=user_color, timestamp=arrow.utcnow().datetime)
    response.set_author(name=msg.author.name, icon_url=avatar)
    response.set_footer(text=f'#{msg.channel.name}')
    response.description = msg.content
    attachments = False
    if msg.attachments:
        enders = ['png', 'jpg', 'gif', 'webp']
        ender = msg.attachments[0].filename.lower().split('.')[-1]
        if ender.split('?')[0] in enders:
            attachments = True
            response.set_image(url=msg.attachments[0].url)
    if not msg.content and not attachments:
        return None
    return response


async def check_emotes(db: Database, mid: int, sbl: int):
    trigger = False
    executed = await db.cache.get_cache(f'exec_{mid}')
    if not executed:
        stars = await db.cache.get_cache(mid) or 0
        stars += 1
        if stars >= sbl:
            trigger = True
            await db.cache.del_cache(mid)
            await db.cache.set_cache(f'exec_{mid}', True)
        else:
            await db.cache.set_cache(mid, stars)
    return trigger


async def starboard_watcher(ev: SigmaEvent, payload: RawReactionPayload):
    payload = payload.raw
    uid = payload.user_id
    cid = payload.channel_id
    mid = payload.message_id
    emoji = payload.emoji
    channel = await ev.bot.get_channel(cid)
    if channel:
        if hasattr(channel, 'guild'):
            guild = channel.guild
            if guild:
                starboard_doc = await ev.db.get_guild_settings(guild.id, 'starboard') or {}
                if starboard_doc:
                    sbc = starboard_doc.get('channel_id')
                    sbe = starboard_doc.get('emote')
                    sbl = starboard_doc.get('limit')
                    if sbc and sbe and sbl:
                        if channel.id != sbc:
                            if emoji.name == sbe:
                                user = guild.get_member(uid)
                                if user:
                                    if not user.bot:
                                        try:
                                            enough = check_emotes(ev.db, mid, sbl)
                                            if enough:
                                                message = await channel.get_message(mid)
                                                if not message.author.bot:
                                                    response = await generate_embed(message)
                                                    if response:
                                                        await post_starboard(message, response, sbc)
                                        except (discord.NotFound, discord.Forbidden):
                                            pass