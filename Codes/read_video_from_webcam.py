# -*- coding: utf-8 -*-
"""
Created on 2021

@author: mntalha
github : https://github.com/mntalha
"""

#Library import 
import cv2 as cv

#0 : webcam
# 1, 2,3 ,... other hooked on cameras
capture = cv.VideoCapture(0)


while True:
    #isTrue : capturing from source whether succesfull or not
    isTrue,frame =capture.read()
    
    #if readed succesfull show video
    if isTrue:
        cv.imshow("Live Video",frame)
    
    #Check every 10 milisecond of keyboard press on "d"
    # this 10 milisecond also is the delay of frame
    if cv.waitKey(10) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()