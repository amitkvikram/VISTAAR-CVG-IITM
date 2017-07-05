#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('paint1.png',0)

ret, img_new= cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
cv2.imshow('image',img_new)
cv2.waitKey(3000)
cv2.destroyAllWindows()
