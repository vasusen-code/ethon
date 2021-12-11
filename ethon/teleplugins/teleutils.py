"""This file is part of the CompressorBot distribution.
Copyright (c) 2021 vasusen-code

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

License can be found in < https://github.com/vasusen-code/ethon/blob/main/LICENSE > ."""

#vasusen-code/thechariotoflight/dronebots
#__TG:ChauhanMahesh__
from telethon import events

async def mention(bot, id):
    a = await bot.get_entity(int(id))
    x = a.first_name
    return f'[{x}](tg://user?id={id})'
    
