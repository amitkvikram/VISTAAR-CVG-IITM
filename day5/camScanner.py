
#!/usr/bin/python
import numpy as np
import cv2
from math import *
from matplotlib import pyplot as plt

img = cv2.imread('polygons.jpg',-1)
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_new= cv2.threshold(img_gray, 210,255 , cv2.THRESH_BINARY_INV)
image, contours, hierarchy = cv2.findContours(img_new,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# cnts= sorted(contours, key= cv2.contourArea, reverse =True)[:5]

print(contours)
