#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('polygons.jpg',-1)
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_new= cv2.threshold(img_gray, 210,255 , cv2.THRESH_BINARY_INV)
image, contours, hierarchy = cv2.findContours(img_new,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
#cv2.imshow('img_gray',img_new)
for i in range(len(contours)):
    x,y,w,h=cv2.boundingRect(contours[i])
    # cv2.rectangle(img_gray,(x,y),(x+w,y+h),(0),2)

    imgX=np.array(img_gray[y-10:y+h+10, x-10:x+w+10])
    img_contour = cv2.drawContours(img_gray, contours, -1, (0,255,0), 3)
    corners = np.int0(cv2.goodFeaturesToTrack(img_contour,6,0.01,10))
    # cv2.imshow('image1',img_contour)
    if cv2.waitKey(0)==27:
         cv2.destroyAllWindows()
    print(corners)
    for num,i in enumerate(corners):
        x,y = i.ravel()
        cv2.circle(imgX,(x,y),10,0,-1)
        cv2.imshow('image1',imgX)
        if cv2.waitKey(0)==27:
            cv2.destroyAllWindows()
print("Total Num of Corners={0}".format(len(corners)))



#cv2.imshow('img_gray',img_gray)

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
# img_contour = cv2.drawContours(img_new, contours, -1, (0,255,0), 3)
