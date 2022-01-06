"""This file is part of the ethon distribution.
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

import os
import pathlib
from youtube_dl import YoutubeDL

#rename files
def rename(source, output):
    os.rename(source, output)
    
#get file extension using path of file
def file_extension(file_path):
    extension = pathlib.Path(f'{file_path}').suffix 
    return extension

#make a list with limited length and check length
#Limit = maximun length of the list
def Q_length(List, limit):
    length = len(List)
    if length > int(limit) + 1:
        return 'FULL'
    else:
        return length
    
#Download videos from youtube
def youtube(url):    
    options = {
        "nocheckcertificate": True,
        "geo-bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best",
        "quiet": True }
    YoutubeDL(options).download([url])
    info = YoutubeDL({}).extract_info(url=url, download=False)
    title = info["title"]
    ext = info["ext"]
    file = title + "." + ext
    return file
