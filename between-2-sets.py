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
    maxa = max(a)
    minb = min(b)
    maxaarr=[]
    arra=[]
    i=1
    try:
        while(maxa*i<=minb):
            maxaarr.append(maxa*i)
            i+=1
        for k in a:
            j=0
            while(maxaarr[j]!=maxaarr[-1]):
                if maxaarr[j]%k==0:
                    arra.append(maxaarr[j])
                    j+=1
                else:
                    if maxaarr[j] in arra:
                        arra.remove(maxaarr[j])
                    maxaarr.remove(maxaarr[j])
            if maxaarr[j]%k==0:
                    arra.append(maxaarr[j])
            else:
                    maxaarr.remove(maxaarr[j])
                    if maxaarr[j] in arra:
                        arra.remove(maxaarr[j])
            arra = list(set(arra))
        res=[]
        for elea in arr:
            count =0
            for eleb in b:
                if eleb%elea == 0:
                    count+=1
            if count == len(b):
                res.append(elea)
        return len(res)
    except:
        return 0
        
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
