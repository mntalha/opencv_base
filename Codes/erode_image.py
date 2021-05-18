# -*- coding: utf-8 -*-
"""
Created on 2021

@author: mntalha
github : https://github.com/mntalha
"""

#Library import 
import cv2 as cv

#Image relative or absolute path
#BGR format.
path  = "../Resources/sample_1.jpg"

#Take image inside 
img = cv.imread(path)

#Show image 
cv.imshow("Sample Image",img)

# Eroding process
#similar to the edging 

eroded = cv.erode(img, (5,5), iterations=2)

#Show image 
cv.imshow('Eroded Image', eroded)


#Wait until closed.
cv.waitKey(0)
