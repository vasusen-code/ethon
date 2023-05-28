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

#to get width, height and duration(in sec) of a video
def videometadata(file):
    vcap = cv2.VideoCapture(f'{file}')  
    width = round(vcap.get(cv2.CAP_PROP_FRAME_WIDTH ))
    height = round(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
    fps = vcap.get(cv2.CAP_PROP_FPS)
    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = round(frame_count / fps)
    data = {'width' : width, 'height' : height, 'duration' : duration }
    return data

# function to find the resolution of the input video file

import subprocess
import shlex
import json

def findVideoResolution(pathToInputVideo):
    cmd = "ffprobe -v quiet -print_format json -show_streams"
    args = shlex.split(cmd)
    args.append(pathToInputVideo)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    ffprobeOutput = subprocess.check_output(args).decode('utf-8')
    ffprobeOutput = json.loads(ffprobeOutput)

    # find height and width
    height = ffprobeOutput['streams'][0]['height']
    width = ffprobeOutput['streams'][0]['width']

    # find duration
    out = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", pathToInputVideo])
    ffprobe_data = json.loads(out)
    duration_seconds = float(ffprobe_data["format"]["duration"])

    return int(height), int(width), int(duration_seconds)

def duration(pathToInputVideo):
    out = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", pathToInputVideo])
    ffprobe_data = json.loads(out)
    duration_seconds = float(ffprobe_data["format"]["duration"])
    return int(duration_seconds)
  
def video_metadata(file):
    height = 720
    width = 1280
    duration = 0
    try:
        height, width, duration = findVideoResolution(file)
        if duration == 0:
            data = videometadata(file)
            duration = data["duration"]
            if duration is None:
                duration = 0
    except Exception as e:
        try: 
            if 'height' in str(e):
                data = videometadata(file)
                height = data["height"]
                width = data["width"]
                duration = duration(file)
                if duration == 0:
                    data = videometadata(file)
                    duration = data["duration"]
                    if duration is None:
                        duration = 0
        except Exception as e:
            print(e)
            height, width, duration = 720, 1280, 0
    data = {'width' : width, 'height' : height, 'duration' : duration }
    return data
