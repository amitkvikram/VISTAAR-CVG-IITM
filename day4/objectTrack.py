#!/usr/bin/python3
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.stats import mode

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
        flag=2
    elif event==cv2.EVENT_MOUSEMOVE and flag==1:
        flag=1
        x1=x
        y1=y
        print([x,y])

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('frame',frame)
cv2.setMouseCallback('frame',draw_rect)
while(True):
    ret, frame = cap.read()
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
    if(flag==1):
        cv2.rectangle(frame,(init_x,init_y),(x1,y1),(0,255,0),1)
    elif(flag==2):
        cv2.rectangle(frame,(init_x,init_y),(final_x, final_y),(0,255,0),1)
    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()
#print("INIT: " , init_x , init_y)
#print("FINAL: ", final_x , final_y)

roi = frame[init_y:final_y,init_x:final_x,:]
print(roi.shape)

newImg = cv2.cvtColor(roi , cv2.COLOR_BGR2HSV)
cv2.imshow("roi" , newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(2,2,1)
plt.hist(newImg[:, :,0] )
plt.subplot(2,2,2)
plt.hist(newImg[:, :,1] )
plt.subplot(2,2,3)
plt.hist(newImg[:, :,2] )
plt.subplot(2,2,4)
plt.imshow(newImg)
plt.show()


H , _ = mode(newImg[:,:,0])
S , _ = mode(newImg[:,:,1])
V , _ = mode(newImg[:,:,2])

print("H: ", H[0,0])
const_var = 4
lower_bound = [H[0,0]-const_var , S[0,0]-2*const_var , V[0,0]-5*const_var]
upper_bound = [H[0,0]+const_var , 255, 255]


print("Lower Bound" , lower_bound)
print(upper_bound)

cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(lower_bound, dtype=np.uint8)
    upper_blue = np.array(upper_bound, dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
