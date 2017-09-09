#!/usr/bin/python3
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img = cv2.imread('/home/amit/Documents/cfi/vistaar-cvg-amit/day6/ps1-input0.png',-1)
img_blur=cv2.GaussianBlur(img,(5,5),1)

edges= cv2.Canny(img, 100, 200)
edges1= cv2.Canny(img_blur, 100, 200)

lines= cv2.HoughLines(edges1, 1 , np.pi/180, 200)
print(lines)
i=0
r,c,k=lines.shape
while(i<r):
    for rho , theta in lines[i]:
        a= np.cos(theta)
        b= np.sin(theta)
        x0= a*rho
        y0= b*rho
        x1= int(x0 + 1000*(-b))
        y1= int(y0 + 1000*(a))
        x2= int(x0 -1000*(-b))
        y2= int(y0 - 1000*(a))

        cv2.line(img_blur, (x1, y1), (x2, y2), (0,0,255), 2)
        i+=1

# cv2.imshow('frame',img_blur)
cv2.imshow('frame2', img_blur)
cv2.imshow('frame1', img)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
