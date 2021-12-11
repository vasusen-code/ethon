import subprocess 
import cv2

#fastest way to get total number of frames in a video
def total_frames(video_path):
    cap = cv2.VideoCapture(f"{video_path}")
    tf = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    return tf        

def bash(cmd):    
    bashCommand = f"{cmd}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE) 
    output, error = process.communicate()
    return output, error
    
