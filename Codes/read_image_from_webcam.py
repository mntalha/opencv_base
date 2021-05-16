# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:57:17 2021

@author: mntalha
github : https://github.com/mntalha
"""

#Library import 
import cv2 as cv

#0 : webcam
# 1, 2,3 ,... other hooked on cameras
capture = cv.VideoCapture(0)

#read only one frame
_,frame = capture.read()

#Show image 
cv.imshow("Sample Image",frame)

#release the capture
capture.release()

#Wait until closed.
cv.waitKey(0)


