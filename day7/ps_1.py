#!/usr/bin/python3
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img= cv2.imread('ps1-input0.png',0)
edges= cv2.Canny(img, 100, 200)
cv2.imshow('frame1',edges)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()

lines= cv2.HoughLines(edges, 1 , np.pi/180, 93)
i=0
r,c,k=lines.shape
while(i<r):
    for rho , theta in lines[i]:
        a= np.cos(theta)
        b= np.sin(theta)
        angle= (round(math.degrees(theta)))
        print(rho,angle)
        x0= a*rho
        y0= b*rho
        x1= int(x0 + 1000*(-b))
        y1= int(y0 + 1000*(a))
        x2= int(x0 -1000*(-b))
        y2= int(y0 - 1000*(a))
        if angle==90:
            cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)
        i+=1
cv2.imshow('frame', img)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
