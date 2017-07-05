#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt


img =cv2.imread('sudokusmall.png', -1)

row,cols, channel= img.shape

pts1=[]
pts2=[]

def INPUT(event, x, y, flags, param):
    if event== cv2.EVENT_LBUTTONDBLCLK:
        if len(pts1)<4:
            pts1.append([x,y])
            print(len(pts1))
        else:
            pts2.append([x,y])


cv2.namedWindow('image')
cv2.setMouseCallback('image',INPUT)
while(1):
    cv2.imshow('image',img)
    if len(pts1)>4 and len(pts2)>4:
        break
    if cv2.waitKey(20)==27:
        break
cv2.destroyAllWindows()

pts1=np.array(pts1).astype('float32')
pts2=np.array(pts2).astype('float32')
print(pts1)
print(pts2)

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols,row))
cv2.imshow('image',dst)
cv2.waitKey(5000)
cv2.destroyAllWindows()
print(pts1)
