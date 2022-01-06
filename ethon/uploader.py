import yt_dlp
import youtube_dl
import requests
import re
import os

#Download videos from youtube-------------------------------------------------------------------------------------------
def download_from_youtube(url):
    options = {
        "prefer_ffmpeg": True,
        "nocheckcertificate": True,
        "geo-bypass": True,
        "outtmpl": "%(id)s.mp4",
        "format": "best",
        "quiet": True }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
        info = ydl.extract_info(url, download=False)
        title = info.get("title", None)
        id = info.get("id", None)
        ext = info.get("ext", None)
        ex = "." + options["outtmpl"].split(".")[-1]
        file = title + "." + ext
        try:
            os.rename(id + ex, file)
        except FileNotFoundError:
            os.rename(id + ex * 2, file)
        return file
      
#for ytdlp supported sites ------------------------------------------------------------------------------------------

#logging
class YTLogger:
    def debug(self, msg):
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        
ydlp_opts={'logger': YTLogger(),
          'outtmpl': '%(title)s.%(ext)s',
          'no_warnings': True, 
          'quiet': True,
          'geo-bypass': True}

def ytdl(url):
    with yt_dlp.YoutubeDL(ydlp_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None) 
        video_ext = info_dict.get('ext', None) 
        return video_title + '.' + video_ext
      
      
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

