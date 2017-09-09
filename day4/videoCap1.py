#!/usr/bin/python
import numpy as np
import cv2
from math import *
from matplotlib import pyplot as plt

init_x=0
init_y=0
final_x=0
final_y=0
flag=0
x1=0
y1=0

def draw_rect(event, x, y, flags, param):
    global init_x
    global init_y
    global final_x
    global final_y
    global flag
    global x1
    global y1
    if event==cv2.EVENT_LBUTTONDOWN:
        init_x=x
        init_y=y
        flag=1
    elif event==cv2.EVENT_LBUTTONUP:
        final_y=y
        final_x=x
        flag=3
    elif event==cv2.EVENT_MOUSEMOVE and flag==1:
        # print("amit")
        flag=1
        x1=x
        y1=y

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('frame',frame)
cv2.setMouseCallback('frame',draw_rect)

while(True):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(flag==1):
        cv2.rectangle(frame,(init_x,init_y),(x1,y1),(0,255,0),3)
    if(flag==3):
        cv2.rectangle(frame,(init_x,init_y),(final_x, final_y),(0,255,0),3)
    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()

HSV_matrix= cv2.cvtColor(frame[init_y:final_y,init_x:final_x,:],cv2.COLOR_BGR2HSV)
Hue_matrix= HSV_matrix[:,:,0]
Sat_matrix= HSV_matrix[:,:,1]
Val_matrix= HSV_matrix[:,:,2]
cv2.imshow('image',HSV_matrix)
cv2.waitKey(1000)
cv2.destroyAllWindows()

plt.subplot(2,2,1)
plt.hist(Hue_matrix)
plt.subplot(2,2,2)
plt.hist(Sat_matrix)
plt.subplot(2,2,3)
plt.hist(Val_matrix)
plt.subplot(2,2,4)
plt.imshow(HSV_matrix)
plt.show()

Hue_matrix=np.array(list(Hue_matrix.flat))
Sat_matrix=np.array(list(Sat_matrix.flat))
Val_matrix=np.array(list(Val_matrix.flat))

Hue_mean=np.sum(Hue_matrix)/len(Hue_matrix)
Sat_mean=np.sum(Sat_matrix)/len(Sat_matrix)
Val_mean=np.sum(Val_matrix)/len(Val_matrix)

Hue_dev=sqrt(np.sum(np.square(Hue_matrix-Hue_mean))/len(Hue_matrix))
Sat_dev=sqrt(np.sum(np.square(Sat_matrix-Sat_mean))/len(Sat_matrix))
Val_dev=sqrt(np.sum(np.square(Val_matrix- Val_mean))/len(Val_matrix))

lower_blue= np.array([Hue_mean-Hue_dev, Sat_mean- Sat_dev, Val_mean-Val_dev]).astype('uint8')
upper_blue=np.array([Hue_mean+Hue_dev, Sat_mean+Sat_dev, Val_mean+Val_dev]).astype('uint8')

cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

cap.release()
cv2.destroyAllWindows()
