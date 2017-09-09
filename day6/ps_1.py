#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img=cv2.imread('ps1-input0.png',0)

#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('src',img)

img_sobelX = cv2.Sobel(img,-1,1,0,ksize=-1)
print(img_sobelX)

img_SobelY=cv2.Sobel(img,-1,0,1,ksize=-1)
print(img_SobelY)
img_scharrX = cv2.Scharr(img,-1,1,0)
img_scharrY=cv2.Scharr(img,cv2.CV_64F,0,1)
img_laplacian=cv2.Laplacian(img,-1,ksize=1)
ret, img_laplacian=cv2.threshold(img_laplacian,1,255,cv2.THRESH_BINARY)
img_canny=cv2.Canny(img,100,200)

#cv2.imshow('sobelX',img_sobelX)
#cv2.waitKey(3000)
#cv2.imshow('sobleY',img_SobelY)
#cv2.imshow('scharrX',img_scharrX)
#cv2.imshow('scharrY',img_scharrY)
cv2.imshow('laplacian',img_laplacian)
cv2.imshow('canny',img_canny)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()

edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()
