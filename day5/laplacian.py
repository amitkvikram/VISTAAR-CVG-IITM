#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img=cv2.imread('sudokusmall.png',-1)

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('src',img)
kernel= np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

dst = cv2.filter2D(img,cv2.CV_64F,kernel)

laplacian = cv2.Laplacian(img,cv2.CV_64F,ksize=1)
cv2.imshow('dst',dst)
cv2.imshow('laplacian',laplacian)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
