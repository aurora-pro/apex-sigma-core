from discord import Embed

async def getreaction(cmd, message, args):
    if not args:
        return

    react_id = args[0].lower()
    react_item = cmd.db[cmd.db.db_cfg.database].Interactions.find_one({'ReactionID': react_id})
    if not react_item:
        return

    response = Embed(color=0x5dadec)
    response.set_image(url=react_item['URL'])
    response.set_footer(text=f'Reaction ID: {react_id}')
    await message.channel.send(embed=response)
