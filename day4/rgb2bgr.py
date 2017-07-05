#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt


img= cv2.imread("lenna.png", -1)
row, column, channel= img.shape
#print(img[0,0][0]) #0.299R + 0.587G +0.114B
matrix=[0.299, 0.587, 0.114]
# matrix=np.tile(np.array([0.299, 0.587, 0.114]),(column,1))

img_new=img.dot(matrix).astype('uint8')

cv2.imwrite('lenna_bgr1.png',img_new)
cv2.imshow('1',img)
cv2.waitKey(5000)
cv2.imshow('1',img_new)
cv2.waitKey(5000)
cv2.destroyAllWindows()
