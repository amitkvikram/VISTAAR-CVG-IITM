#!/usr/bin/python3.5
if __name__ == '__main__':
    array=[]
    for i in range(1000,3001):
        temp=str(i)
        temp.split()
        found=0
        for j in temp:
            if(int(j)%2!=0):
                 found=1;
        if(found==0):
            array.append(i)

    print(*array,sep=",")
