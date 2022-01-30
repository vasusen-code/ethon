#ignore this file

from telethon import events, Button


async def start_srb(event):
    await event.reply("Send me Link of any message to clone it here, For private channel message, send invite link first.\n\n**SUPPORT:** @TeamDrone", 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("DEV", url="t.me/MaheshChauhan")]])
                              
    
