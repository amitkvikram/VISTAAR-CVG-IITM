#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img= cv2.imread("lenna.png", -1)

row, column, channel= img.shape
# print(img.shape)
img_new=np.empty_like(img)
img1=np.zeros((row//2,column//2))
print(img_new.shape)
img_new[0:row//2,0:column//2:,:]= img[0:row//2,0:column//2,:] *[1,0,0]
img_new[row//2:row,0:column//2,:]=img[row//2:row,0:column//2,:]*[0,0,1]
img_new[0:row//2, column//2:column,:]=img[0:row//2, column//2:column,:]*[0,1,0]
img1=(img[row//2:row, column//2:column,:].dot([0.299, 0.587, 0.114])).astype('uint8')
img_new[row//2:row, column//2:column,:]=cv2.merge((img1,img1,img1))
cv2.imshow('image1',img_new)
cv2.waitKey(8000)
#cv2.imwrite('p.png',img_new)
cv2.destroyAllWindows()
