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

import subprocess 
import cv2

#fastest way to get total number of frames in a video
def total_frames(video_path):
    cap = cv2.VideoCapture(f"{video_path}")
    tf = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    return tf        

#makes a subprocess handy
def bash(cmd):    
    bashCommand = f"{cmd}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE) 
    output, error = process.communicate()
    return output, error
    
