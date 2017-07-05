#!/usr/bin/python
from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt



def event_():

    event=[i for i in dir(cv2) if 'EVENT' in i]
    print(event)

def draw_circle(event, x, y, flags, param):
    if event== cv2.EVENT_LBUTTONDBLCLK:
        if x<=row/2 and y<=column/2:
            x=int(row/4)
            y=int(column/4)
            cv2.circle(img,(x,y), 100, (255,0,0), -1)
        elif x>row/2 and y<=column/2:
            x=int(row*.75)
            y=int(column*.25)
            cv2.circle(img,(x,y), 100, (0,255,0), -1)
        elif x<row/2 and y>column/2:
            print([x,y])
            x=int(row*.25)
            y=int(column*.75)
            cv2.circle(img,(x,y), 100, (0,0,255), -1)
        elif x>row/2 and y>column/2:
            x=int(row*.75)
            y=int(column*.75)
            cv2.circle(img,(x,y), 100, (255,255,255), -1)





img= cv2.imread('lenna.png',-1)
global row
global column
row = img.shape[0]
column=img.shape[1]
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)==27:
        break
cv2.destroyAllWindows()
