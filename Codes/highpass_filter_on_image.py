# -*- coding: utf-8 -*-
"""
Created on  2021

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


#-------  Laplacian Derivatives -------

laplacian = cv.Laplacian(img,cv.CV_64F)


#Show image 
cv.imshow("Laplacian Image",laplacian)

#---------------------------------

#-------  Sobel x  -------

sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)

#Show image 
cv.imshow("Sobel-x Image",sobelx)
#---------------------------------

#-------  Sobel y  -------

sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

#Show image 
cv.imshow("Sobel-y Image",sobely)

#---------------------------------

#-------  Canny   -------

canny = cv.Canny(img,125,150)

#Show image 
cv.imshow('Canny Edges', canny)

#---------------------------------
#Wait until closed.
cv.waitKey(0)
