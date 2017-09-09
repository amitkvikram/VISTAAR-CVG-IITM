#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img=cv2.imread('polygons.jpg',-1)
cv2.imshow('image1',img)
img_blur=cv2.GaussianBlur(img,(5,5),0)
# blur = cv2.blur(img,(5,5))
# print(cv2.getGaussianKernel())
kernel=np.ones((5,5))/25
blur=cv2.filter2D(img,-1,kernel)
cv2.imshow('blur',blur)
cv2.imshow('Gaussianblur',img_blur)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
