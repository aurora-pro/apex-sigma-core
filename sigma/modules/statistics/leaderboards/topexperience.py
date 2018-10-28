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
from humanfriendly.tables import format_pretty_table as boop

from sigma.core.mechanics.command import SigmaCommand
from sigma.core.mechanics.payload import CommandPayload
from sigma.modules.moderation.server_settings.filters.edit_name_check import clean_name
from sigma.modules.statistics.leaderboards.topcookies import get_leader_docs


async def topexperience(cmd: SigmaCommand, pld: CommandPayload):
    message, args = pld.msg, pld.args
    value_name = 'Experience'
    resource = 'experience'
    sort_key = f'ranked'
    lb_category = 'This Month\'s'
    localed = False
    if args:
        if args[0].lower() == 'total':
            sort_key = 'total'
            lb_category = 'Total'
        elif args[0].lower() == 'local':
            sort_key = f'origins.guilds.{message.guild.id}'
            lb_category = message.guild.name
            localed = True
    now = arrow.utcnow().timestamp
    leader_docs = await cmd.bot.cache.get_cache(sort_key)
    leader_timer = await cmd.bot.cache.get_cache(f'{sort_key}_stamp') or now
    if not leader_docs or leader_timer + 180 < now:
        coll = cmd.db[cmd.db.db_nam][f'{resource.title()}Resource']
        search = {'$and': [{sort_key: {'$exists': True}}, {sort_key: {'$gt': 0}}]}
        all_docs = await coll.find(search).sort(sort_key, -1).limit(100).to_list(None)
        leader_docs = await get_leader_docs(cmd, message, localed, all_docs, sort_key)
        await cmd.db.cache.set_cache(sort_key, leader_docs)
        await cmd.db.cache.set_cache(f'{sort_key}_stamp', now)
    table_data = [
        [
            pos + 1 if not doc[0].id == message.author.id else f'{pos + 1} <',
            clean_name(doc[0].name, 'Unknown')[:12],
            str(int(doc[1] / 13266.85)),
            str(doc[1])
        ] for pos, doc in enumerate(leader_docs)
    ]
    table_body = boop(table_data, ['#', 'User Name', 'Level', value_name])
    response = f'🔰 **{lb_category} {value_name} Leaderboard**'
    response += f'\n```hs\n{table_body}\n```'
    response += f'\nLeaderboard last updated {arrow.get(leader_timer).humanize()}.'
    await message.channel.send(response)
