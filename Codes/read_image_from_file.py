# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:49:13 2021

@author: talha
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

#Wait until closed.
cv.waitKey(0)
