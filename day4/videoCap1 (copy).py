#!/usr/bin/python
import numpy as np
import cv2

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
        # print("amit")
        init_x=x
        init_y=y
        flag=1

    elif event==cv2.EVENT_LBUTTONUP:
        final_y=y
        final_x=x
        flag=3
        # cv2.rectangle(frame,(init_x,init_y),(final_x, final_y),(0,255,0),3)
    elif event==cv2.EVENT_MOUSEMOVE and flag==1:
        # print("amit")
        flag=1
        x1=x
        y1=y
        print([x,y])
        # cv2.rectangle(frame,(init_x,init_y),(x,y),(0,255,0),3)
    # cv2.imshow('frame',frame)



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
        # cv2.setMouseCallback('frame',draw_rect)
        print([x1,y1])
    if(flag==3):
        cv2.rectangle(frame,(init_x,init_y),(final_x, final_y),(0,255,0),3)
    cv2.imshow('frame',frame)


cv2.setMouseCallback('frame',draw_rect)
cap.release()
cv2.destroyAllWindows()
