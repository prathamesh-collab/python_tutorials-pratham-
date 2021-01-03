#!/usr/bin/env python2.7

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #to change the color of frame

    cv2.imshow('frame',frame)   #image show as frame
    #cv2.imshow('gray',gray )  # apply the chang color to the image 
    if cv2.waitKey(20) & 0xFF == ord('q'):



        break


