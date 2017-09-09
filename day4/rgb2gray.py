#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt


img= cv2.imread("lenna.png", -1)
row, column, channel= img.shape
#print(img[0,0][0]) #0.299R + 0.587G +0.114B

matrix1=[0.114, 0.587, 0.299] #CORRECT
matrix2=[0.299, 0.587, 0.114]

img_new1=img.dot(matrix1).astype('uint8')
img_new2=img.dot(matrix2).astype('uint8')
cv2.imwrite('lenna_bgr1.png',img_new1)
cv2.imshow('1',img_new1)
cv2.imshow('2',img_new2)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()


#THEORY:
#Human perceive green more strongly than red and red more than blue.
