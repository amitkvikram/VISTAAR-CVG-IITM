#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img= cv2.imread('field.jpg',0)
template=cv2.imread('template.jpg',0)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img2= img.copy()
    method= eval(meth)
    img_match=cv2.matchTemplate(img2, template,method)

    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(img_match)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left= min_loc
    else:
        top_left = max_loc
    bottom_right =(top_left[0]+w, top_left[1]+h)
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(img_match,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
