#!/usr/bin/python
#Harris Corner Detector in OpenCV
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img=cv2.imread('img1.jpg',-1)

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst= np.float32(img)
dst= cv2.cornerHarris(img,2,3,.04) #img->src 2->neighourhood 3->ksize 0.04->Harris detector parameter
print(dst)
dst = cv2.dilate(dst,None)
img1=cv2.merge((img,img,img))
img2=img1
img1[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('image1',img1)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
corners=cv2.goodFeaturesToTrack(img,1000,0.01,10) #img->src, 1000->mx num of pts, 10->min distance b/w pts
corners=np.int0(corners)


for i in corners:
    x,y= i.ravel()
    cv2.circle(img, (x,y), 3, ([0,255,0]), -1)
cv2.imshow('image1',img)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
