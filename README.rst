ethon
=====

• Telegram_
• Github_

install
=======

.. code:: python
    
    pip install ethon

``ethon.pyutils``

.. code:: python

    from ethon.pyutils import rename, file_extension, youtube
    
    #rename files
    file = 'name of your file'
    path = 'new name for your file'
    rename(file, path) 
    
    #get file extension using path of file
    path = 'path of your file'
    extension = file_extension(path)
    
    #Download videos from youtube
    filename = youtube(url)

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

.. _Telegram: https://t.me/MaheshChauhan
.. _Github : https://Github.com/Vasusen-code
