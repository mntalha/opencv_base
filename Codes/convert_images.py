# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:53:38 2021

@author: mntalha
github :https://github.com/mntalha
"""

#Library import 
import cv2 as cv

#Image relative or absolute path
#BGR format automatically
path  = "../Resources/sample_1.jpg"

#Take image inside 
img = cv.imread(path)

#Show BGR image 
cv.imshow("BGR Image",img)


#-------  from BGR to RGB -------

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#Show RGB image 
cv.imshow("RGB Image",rgb)

#matplotlib also shows RGB automatically
import matplotlib.pyplot as plt
plt.title("RGB Image of Matplotlib")
plt.imshow(img)
plt.show()

#---------------------------------


#-------  from BGR to GRAY -------

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Show Gray image 
cv.imshow("Gray Image",gray)

#---------------------------------

#-------  from BGR to HSV -------

#preferred in color detection

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Show HSV image 
cv.imshow("HSV Image",hsv)

#---------------------------------

#-------  from BGR to LAB -------

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

#Show LAB image 
cv.imshow("LAB Image",lab)

#---------------------------------
#Wait until closed.
cv.waitKey(0)