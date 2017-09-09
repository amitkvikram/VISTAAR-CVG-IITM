#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img = cv2.imread('images.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)
# cv2.imshow('frame',edges)
# if cv2.waitKey(0)==27:
    # cv2.destroyAllWindows()
lines = cv2.HoughLines(edges,1,np.pi/180,10) #edges->edges; 1->rho accuracies ; np.pi/180->angle accuracies; 200->min length for line
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('houghlines3.jpg',img)
