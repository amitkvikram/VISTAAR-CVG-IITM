#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img =cv2.imread('lenna.png', -1)
cv2.imshow('image',img)
cv2.waitKey(2000)

row,cols, channel= img.shape

M=np.float32([[1,0,20],[0,1,10]])
dst= cv2.warpAffine(img,M,(cols,row))

cv2.imshow('image',dst)
cv2.waitKey(2000)
cv2.destroyAllWindows()
