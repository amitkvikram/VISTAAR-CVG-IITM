#!/usr/bin/python3.5
if __name__ == '__main__':
    sum=0;
    str=input()
    #print(str)
    while str!='!':
        a, b=str.split(" ")
        if(a=='D'):
             sum= sum+int(b)
        else:
            sum=sum-int(b)
        str=input()
    print(sum)
