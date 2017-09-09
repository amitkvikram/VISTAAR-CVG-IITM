#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img=cv2.imread('lenna.png',-1)

red=np.array(img[:,:,2])
print(red)
plt.hist(red.flat, bins=256)
plt.show()
