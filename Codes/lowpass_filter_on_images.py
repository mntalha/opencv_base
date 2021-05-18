# -*- coding: utf-8 -*-
"""
Created on 2021

@author: mntalha
github : https://github.com/mntalha
"""

#Low pass  == smoothing == blurring 

# The purpose is to smooth the images.

# Edges decline.

#helps reduce the noise


#Library import 
import cv2 as cv
import numpy as np

#Image relative or absolute path
#BGR format.
path  = "../Resources/sample_1.jpg"

#Take image inside 
img = cv.imread(path)

#Show image 
cv.imshow("Sample Image",img)

#-------  Gaussian -------
# Gaussian kernel is used
#applied filter size
kernel_size = (5,5)

#methods
gaussian = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)

#Show Gaussian image 
cv.imshow('Gaussian Image', gaussian)

#---------------------------------

#-------  Convolution  -------
#applied filter size 5x5
kernel_size = np.ones((5,5),np.float32)/25

#methods
convol = cv.filter2D(img,0,kernel_size)

#Show Gaussian image 
cv.imshow('Convolved Image', convol)

#---------------------------------


#-------  Averaging  -------
#applied filter size
kernel_size = (5,5)

blur = cv.blur(img,kernel_size)

#Show Averaging image 
cv.imshow('Averaging Image', blur)
#---------------------------------

#-------  Median  -------

median = cv.medianBlur(img,5)

#Show Median image 
cv.imshow('Median Image', median)
#---------------------------------

#-------  Bilateral  -------
#highly effective while keeping edges sharp

# in gauss , it blurs the edges but in bilateral it is considered
bilateral = cv.bilateralFilter(img,5,75,75)

#Show Bilateral image 
cv.imshow('Bilateral Image', bilateral)
#---------------------------------

#Wait until closed.
cv.waitKey(0)


