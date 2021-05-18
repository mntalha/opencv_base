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
cv.imshow('Sample Image', img)

print(f'Image shape is : ({img.shape[1]}x{img.shape[0]})')

#x coordinates
x_start = 150
x_end = 350

#y coordinates
y_start = 200
y_end = 300

crop = img [x_start:x_end,y_start:y_end]
cv.imshow('Cropped Image', crop)

#Wait until closed.
cv.waitKey(0)