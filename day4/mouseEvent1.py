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
        cv2.circle(img,(x,y), 100, (255,0,0), -1)
        prin
