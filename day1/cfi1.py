#!/usr/bin/python3.5
if __name__ == '__main__':
    print("Enter no. of test cases")
    t=int(input())
    while t:

        print("Enter the number")
        n=int(input())
        temp=1;
        for i in range(1,n+1):
            temp*=i;

        print(temp)
        t=t-1;
