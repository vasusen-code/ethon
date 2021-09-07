async def mention(bot, id):
    a = await bot.get_entity(int(id))
    x = a.first_name
    return f'[{x}](tg://user?id={id})'
    
