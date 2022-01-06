import yt_dlp
import requests
import re
import os
import subprocess

def bash(cmd):    
    bashCommand = f"{cmd}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE) 
    output, error = process.communicate()
    return output, error

#Download videos from youtube-------------------------------------------------------------------------------------------
def download_from_youtube(url):
    bash(f'yt-dlp -f best --no-warnings -o %(title)s.%(ext)s {url}')
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = info.get("title", None)
        video_ext = info.get("ext", None) 
        return video_title + "." + video_ext
    
#for ytdlp supported sites ------------------------------------------------------------------------------------------

def ytdl(url):
    if 'HLS' in url:
        bash(f'yt-dlp -f best --no-warnings --hls-prefer-ffmpeg -o %(title)s.%(ext)s {url}')
    elif 'm3u8' in url:
        bash(f'yt-dlp -f best --no-warnings --hls-prefer-ffmpeg -o %(title)s.%(ext)s {url}')
    else:
        bash(f'yt-dlp -f best --no-warnings -o %(title)s.%(ext)s {url}')
    with yt_dlp.YoutubeDL({}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None) 
        video_ext = info_dict.get('ext', None) 
        return video_title + "." + video_ext
    
#weburl download------------------------------------------------------------------------------

#Does the url contain a downloadable resource
def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

#Get filename from content-disposition
def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]
  
def weburl(url):
    x = is_downloadable(url)
    if x is False:
        return None
    elif x is True:
        pass
    else:
        return None
    r = requests.get(url, allow_redirects=True)
    filename = get_filename_from_cd(r.headers.get('content-disposition'))
    open(filename, 'wb').write(r.content)
    return filename

