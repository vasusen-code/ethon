import math
import time
from .FasterTg import upload_file, download_file
from telethon import events

#Fast upload/download methods:

def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if tmp.endswith(":"):
        return tmp[:-1]
    else:
        return tmp
      
def hbs(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "B", 1: "K", 2: "M", 3: "G", 4: "T", 5: "P"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

async def progress(current, total, event, start, type_of_ps, file=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current) / speed) * 1000
        progress_str = "`[{0}{1}] {2}%`\n\n".format(
            "".join(["█" for i in range(math.floor(percentage / 5))]),
            "".join(["" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = (
            progress_str
            + "{0} of {1}\n\nSpeed: {2}/s\n\nETA: {3}\n\n".format(
                hbs(current),
                hbs(total),
                hbs(speed),
                time_formatter(time_to_completion),
            )
        )
        if file:
            await event.edit(
                "{}\n\n`File Name: {}\n\n{}".format(type_of_ps, file, tmp)
            )
        else:
            await event.edit("{}\n\n{}".format(type_of_ps, tmp))

#Why these methods? : Using progress of telethon makes upload/download slow due to callbacks
#these method allows to upload/download in fastest way with progress bars.

async def fast_upload(file, name, time, bot, event, msg):
    with open(file, "rb") as f:
        result = await upload_file(
            client=bot,
            file=f,
            name=name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    time,
                    msg,
                ),
            ),
        )
    return result
  
async def fast_download(filename, file, bot, event, taime, msg):
    with open(filename, "wb") as fk:
        result = await download_file(
            client=bot,
            location=file,
            out=fk,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    taime,
                    msg,
                ),
            ),
        )
    return result
  
