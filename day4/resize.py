#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img =cv2.imread('lenna.png')
cv2.imshow('image',img)
cv2.waitKey(2000)

res= cv2.resize(img, None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)

cv2.imshow('image',res)
cv2.waitKey(5000)
cv2.destroyAllWindows()
