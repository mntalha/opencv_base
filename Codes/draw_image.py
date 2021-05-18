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

#-------  Particular Region Change  -------

#particular color at some region
#Blue,Green,Red
# 0 , 255 , 0 : Green 

#copy image
img_particular = img

img_particular[100:200,200:300]=0,255,0

#Show green image 
cv.imshow('Image with Green part', img_particular)

#---------------------------------

#-------  Add Rectangle   -------
# thickness  = 0,1,2,....
# thickness = -1  fill all 
thickness = 1

#start position
start_pos = (0,0)

#end position
#shape[1] : x shape[0] :y in coordinate system
end_pos = (img.shape[1]// 2 , img.shape[0] // 2)

#color of rectange
#Blue,Green,Red
# 255 , 0 , 0 : Blue 
rect_col = (255, 0, 0)

cv.rectangle(img, start_pos, end_pos, rect_col, thickness=thickness)

#Show rectangle image 
cv.imshow('Image with rectangle part', img)

#---------------------------------

#-------  Add Circle   -------
#color of rectange
#Blue,Green,Red
# 0 , 0 , 255 : Red 
rect_col = (0, 0, 255)

#center

center = (img.shape[1]// 2 , img.shape[0] // 2)

#Radius
radius = 100

cv.circle(img, center,radius , rect_col, thickness=thickness)


#Show Circle image 
cv.imshow('Image with Circle part', img)

#---------------------------------

#-------  Add line   -------


cv.line(img, start_pos, end_pos, rect_col, thickness=thickness)

#Show Line image 
cv.imshow('Image with Line part', img)
#---------------------------------

#-------  Add Text   -------

#text position
pos = (0,250)

# thickness  = 0,1,2,....
thickness = 2

#font size
fontScale = 1

text = "HELLO WORLD"

cv.putText(img, text, pos, cv.FONT_HERSHEY_SIMPLEX,fontScale, rect_col,thickness,cv.LINE_AA)

#Text Image
cv.imshow('Image with Line Text', img)
#---------------------------------


#Wait until closed.
cv.waitKey(0)
