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

#parameters
width = 200
height = 200


# Resize

# cv.INTER_AREA : resampling using pixel area relation.
resized = cv.resize(img, (width,height), interpolation=cv.INTER_AREA)
cv.imshow('Resized Image', resized)


#Wait until closed.
cv.waitKey(0)
