#!/usr/bin/python3.5
import numpy as np
from numpy import linalg
fname="July4Python/dat2.txt"
data=np.loadtxt(fname)
Y=data[:]
n=Y.shape[0]
Y=np.reshape(Y,(n,1))
X1=np.arange(1,n+1)
np.reshape(X1,(200,1))
X0=np.full((200),1)
X=np.array([X0[:],X1[:]])
X=X.T
theta=np.zeros(n).T
theta=(linalg.pinv((X.T).dot(X))).dot((X.T).dot(Y))
print(X)
print(Y)
print(theta)
