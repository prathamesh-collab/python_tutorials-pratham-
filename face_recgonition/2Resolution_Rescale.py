#!/usr/bin/env python2.7

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3,1920) #3:-width

    cap.set(4,1080) #4:- is height
def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)
def change_res(width,height):
    cap.set(3,width)
    cap.set(4,height)

## all abour rescale the frame ------------
def rescale_frame(frame,percent=75):
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent / 100 )
    height = int(frame.shape[0] * scale_percent / 100 )
    dim = (width ,height)
    return cv2.resize(frame,dim,interpolation = cv2.INTER_AREA)
make_1080p()   # calling our function to shpe the frame  

while(True):
    ret , frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

