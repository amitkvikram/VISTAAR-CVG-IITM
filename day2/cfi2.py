#!/usr/bin/python3.5
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import sys
print(sys.argv[0])
data=np.loadtxt(sys.argv[1])
Y=data[:]
LEN=Y.shape[0]
X=np.arange(1,LEN+1)
sum_X=X.sum()
sum_Xsqr=np.square(X).sum() #Element Wise Square
sum_Y=Y.sum()
sum_XY=np.multiply(X,Y).sum() #Matrix Multiplication ElementWise
matrix1=np.array([[LEN, sum_X], [sum_X, sum_Xsqr]])
matrix2=np.array([sum_Y,sum_XY])
[a,b]=linalg.pinv(matrix1).dot(matrix2) #Matrix Multiplication
str="INTERCEPT:"+str(a)+"\n"+"SLOPE:"+str(b)
print(str)

fout=open(sys.argv[1].split()[0]+"answer.txt",'w')
fout.write(str)

A=np.array([np.min(X), np.max(X)])
B=[b*i+a for i in A]
plt.scatter(X,Y,color='r')
plt.plot(A,B)
plt.show()
