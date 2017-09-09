#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

def transfor(img,a,b,c,d):
    print((d-c))
    print((b-a))

    m= (float(d -c )/(b-a))
    img1=(m*(img-a))+c
    print(m)
    img1=img1.astype('uint8')

    return img1

img=cv2.imread('lenna.png',-1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img)

a=20
b=220
c=75
d=100
plt.subplot(2,1,1)
img1=transfor(img,a,b,c,d)
plt.hist(img.flat, bins=256)
cv2.imshow('image1',img1)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
plt.subplot(2,1,2)
plt.hist(img1.flat, bins=256)
plt.show()
