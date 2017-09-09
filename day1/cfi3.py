#!/usr/bin/python3.5
if __name__ == '__main__':
    a, b=map(int, input().split(","))
    array=[[i*j for j in range(b)] for i in range(a)]
    print(array)
