#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    def lcm(x,y):
        if a>b:
            z = x
        elif x<y:
            z = y
        for i in range(z, x*y+1):
            if i%x==0 and i%y==0:
                return i
            
    def hcf(x,y):
        if x<y:
            z=x
        elif x>y:
            z=y
        for j in range(z,1,-1):
            if x%j==0 and y%j==0:
                return j
    
    for k in range(len(a)-1):
        lcma=lcm(a[k],a[k+1])
        a[k+1]=lcma

    for l in range(len(b)-1):
        hcfb = hcf(b[l],b[l+1])
        b[k+1]=hcfb
    
    count = 0
    c=1
    while(lcma*c<=hcfb):
        m=lcma*c
        if hcfb%m==0:
            count+=1
        c+=1
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
