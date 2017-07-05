#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt


img= cv2.imread("lenna.png", -1)
row, column, channel= img.shape
B,G,R= img[:,:,0], img[:,:, 1], img[:,:, 2]
matrix=[0.299, 0.587, 0.114]
B=(0.299*B)
R=(0.114*R)
G=(0.587*G)
img_gray=(B+G+R).astype('uint8')

cv2.imshow('image',img_gray)
cv2.waitKey(2000)
cv2.destroyAllWindows()
