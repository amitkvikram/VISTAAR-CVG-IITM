#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img =cv2.imread('lenna.png', -1)
cv2.imshow('image',img)
cv2.waitKey(2000)
row,cols, channel= img.shape

M=cv2.getRotationMatrix2D((cols/2,row/2),90,1.5)#(cols/2,row/2)->Centre of rotattion; 90->angle
                                                #1.5->isotropic scale factor, M->The output affine transformation, 2x3 floating-point matrix.
dst=cv2.warpAffine(img, M,(cols,row))

cv2.imshow('image',dst)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
