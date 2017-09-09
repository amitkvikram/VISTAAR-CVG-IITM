#!/usr/bin/python3.5
if __name__ == '__main__':
    n=int(input())
    sum=0
    for i in range(1,n+1):
        sum=sum+(i/(i+1))
    print("%.2f" %(sum))
