#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('paint1.png',0)

ret, img_new= cv2.threshold(img, 240, 255, cv2.THRESH_BINARY) #img_new->output image; img->src image
cv2.imshow('image',img_new)
cv2.waitKey(3000)
cv2.destroyAllWindows()


#ret, img_new= cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
#img_new->output image; img->src image
#240->threshold value. 255->maxVal
#cv2.THRESH_BINARY->{maxval if src (x, y) > thresh.... otherwise 0}
#cv2.THRESH_BINARY_INV-> opposite behaviour of cv2.THRES-BINARY_INV

#*****cv2.threshold only applies to single-channel array
