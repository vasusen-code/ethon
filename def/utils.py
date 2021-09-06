async def mention(bot, id):
    a = await bot.get_entity(int(id))
    x = a.first_name
    return [{x}](tg://user?id={id})
    
def name(x):
    file = x.media
    name = x.file.name
    return name
