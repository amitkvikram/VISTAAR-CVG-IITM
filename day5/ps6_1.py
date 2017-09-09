#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img=cv2.imread('polygons.jpg',-1)
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_new= cv2.threshold(img_gray, 210,255 , cv2.THRESH_BINARY_INV)
image, contours, hierarchy = cv2.findContours(img_new,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


for i in range(len(contours)):
    x,y,w,h=cv2.boundingRect(contours[i])
    imgX=np.array(img_gray[y:y+h, x:x+w])
    epsilon = (0.01*cv2.arcLength(contours[i],True))
    approx = cv2.approxPolyDP(contours[i],epsilon,True)
    pts_num=approx.shape[0]
    a=approx[1,0,:]- approx[0, 0,:]
    b=approx[pts_num-1,0,:]- approx[0, 0,:]
    CROSS=np.cross(a,b)
    DOT=np.dot(a,b)
    if DOT!=0:
        angle=math.degrees(math.atan(CROSS/DOT))
        print(angle)
    else:
        print(90)
    for j in range(1,pts_num-1):
        a=approx[j+1,0,:]- approx[j, 0,:]
        b=approx[j-1,0,:]- approx[j, 0,:]
        CROSS=np.cross(a,b)
        DOT=np.dot(a,b)
        if DOT!=0:
            angle=math.degrees(math.atan(CROSS/DOT))
            print(angle)
        else:
            print(90)
    a=approx[0,0,:]- approx[pts_num-1, 0,:]
    b=approx[pts_num-2,0,:]- approx[pts_num-1, 0,:]
    CROSS=np.cross(a,b)
    DOT=np.dot(a,b)
    if DOT!=0:
        angle=math.degrees(math.atan(CROSS/DOT))
        print(angle)
    else:
        print(90)
    # print(approx.shape)

    for i in approx:
        x,y = i.ravel()
        cv2.circle(img_gray,(x,y),10,0,-1)
    print("Next Polygon:")

cv2.imshow('image1',img_gray)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
