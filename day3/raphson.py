#!/usr/bin/python3.5
import numpy as np
import sys
import matplotlib.pyplot as plt
from numpy import linalg
import math


class Saturn:
    iteration=20
    i=0
    def __init__(self, arg1):
        self.t1= arg1
        self.M0=2.8 * 1e6
        self.m=13.3 * 1e3
        self.g=9.81
        self.t2=(self.M0/self.m)-1
        self.u=2510

    def bisection(self):
        while(self.i<self.iteration):
            if(self.funcValue((self.t1+self.t2)/2)==335):
                self.t1=(self.t1+self.t2)/2
                break
            self.t1,self.t2= self.update(self.t1,self.t2)
            self.i+=1
        print(self.t1)

    def update(self,a,b):
        x=(a+b)/2
        if self.funcValue(x)>0:
            b=x
        else:
            a=x
        return (a,b)

    def funcValue(self,t):
        v=self.u*(math.log(self.M0/(self.M0-self.m *t)))-self.g*t-335
        return v

    def funcDerivative(self, t):
        v= (self.u*self.m/(self.M0-self.m*t))-self.g
        return v

    def NewtonRaphson(self):
        found=False
        while self.i<10:
            if self.funcDerivative(self.t2)<1e-14:
                break

            temp=self.t2-(self.funcValue(self.t2)/self.funcDerivative(self.t2))
            #print(temp)
            if abs(temp-self.t2)<0.0001:
                found=True
                break
            self.t2=temp
            self.i+=1
        if found==True:
            print(self.t2)
        else:
            print("Newton Method didn't work")

    def Secant(self):
        while self.i<self.iteration:
            temp=self.t2-self.funcValue(self.t2)*((self.t2-self.t1)/(self.funcValue(self.t2)-self.funcValue(self.t1)))
            if(abs(temp-self.t2)<0.0001):
                self.t2=temp
                break
            self.i+=1
            self.t1=self.t2
            self.t2=temp
        print(self.t2)


time= Saturn(0.00000001)
if len(sys.argv)==2:
    if sys.argv[1]=='1':
        time.bisection()
    elif sys.argv[1]=='2':
        time.NewtonRaphson()
    elif sys.argv[1]=='3':
        time.Secant()
    else:
        print("...")
