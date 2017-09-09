#!/usr/bin/python3.5
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

fname=input()
data=np.loadtxt(fname)
X=data[:,0]
Y=data[:,1]

LEN=X.shape[0]
#print(len)
sum_X=X.sum()
sum_Xsqr=np.square(X).sum()
sum_Y=Y.sum()
sum_XY=np.multiply(X,Y).sum()
matrix1=np.array([[LEN, sum_X], [sum_X, sum_Xsqr]])
matrix2=np.array([sum_Y,sum_XY])
[a,b]=linalg.pinv(matrix1).dot(matrix2)
str="INTERCEPT:"+str(a)+"\n"+"SLOPE:"+str(b)
print(str)

fout=open(fname.split()[0]+"answer.txt",'w')
fout.write(str)


A=np.array([np.min(X),np.max(X)])
B=[b*i +a for i in A]
plt.scatter(X,Y,color='r')
plt.plot(A,B)
plt.show()
