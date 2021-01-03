#!/usr/bin/env python2.7

import numpy as np
import os
import cv2

filename = 'my_recoded_video.avi'
frames_per_second = 24.0
res = '720p'

#set resolution for the video capture
def change_res(cap,width,height):
    cap.set(3,width)
    cap.set(4,width)

# Standard video Dimesion sizes 

STD_DIMENSIONS = {
        "480p":(640,480),
        "720p":(1280,720),
        "1080p":(1920,1080),
        "4K":(3840,2160),
}

# grab resoluation dimensions and set video capture to it 

def get_dims(cap,res='1080p'):
    width,height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
        # change the current capture device 
        # to the resulting resluation 
        change_res(cap,width,height)
        return width , height 

#video encoding 

VIDEO_TYPE = {
        'avi':cv2.VideoWriter_fourcc(*'XVID'),
        'mp4':cv2.VideoWriter_fourcc(*'XVID'),
        }
def get_video_type(filename):
    filename,ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename,get_video_type(filename),25,get_dims(cap,res))

while True:
    ret ,frame = cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()




