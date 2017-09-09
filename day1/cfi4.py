#!/usr/bin/python3.5
if __name__ == '__main__':
    a=input().split(",")
    a.sort()
    print(*a,sep=",")
