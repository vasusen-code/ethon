ethon
=====

• Telegram_
• Github_

install
=======

.. code:: python
    
    pip install ethon

Usage
=====

``ethon.pyutils``

.. code:: python

    from ethon.pyutils import rename, file_extension
    
    #rename files
    rename(file, new_path) 
    
    #get file extension using path of file
    extension = file_extension(file)
    
``ethon.pyfunc``

.. code:: python

    from ethon.pyfunc import bash, total_frames, video_metadata
    
    #handy subprocess
    o, e = bash(cmd)
    
    #get total number of frames in a video
    tf = total_frames(file)
    
    #get basic metadata of video
    data = video_metadata(file)
    
    height = data["height"]
    width = data["width"]
    duration = data["duration"]
    
``ethon.uploader``

.. code:: python

    from ethon.uploader import download_from_youtube, ytdl, weburl
    
    #Download videos from youtube
    filename = await download_from_youtube(url)
    
    #Download videos from YtDlp supported sites
    filename = await ytdl(url)
    
    #Download files from the web
    filename = weburl(url)

.. _Telegram: https://t.me/MaheshChauhan
.. _Github : https://Github.com/Vasusen-code
