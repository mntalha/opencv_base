# -*- coding: utf-8 -*-
"""
Created on 2021

@author: mntalha
github : https://github.com/mntalha
"""

#Library import 
import cv2 as cv

# Taking Snap

video_path = "../Resources/sample_video.mp4" 

#0 : webcam
# 1, 2,3 ,... other hooked on cameras
capture = cv.VideoCapture(video_path)


while True:
    #isTrue : capturing from source whether succesfull or not
    isTrue,frame =capture.read()
    
    #if readed succesfull show video
    if isTrue:
        cv.imshow("Live Video",frame)
    else:
        break
    
    #Check every ~40 milisecond of keyboard press on d
    #this ~40 milisecond also is the delay of frame
    #24 frame in second.
    if cv.waitKey(1000//24) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

