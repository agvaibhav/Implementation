#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    index=[]
    for i in range(n):
        index.append(i)
    cmb=list(itertools.permutations(index,2))
    count=0
    for j in cmb:
        if j[0]<j[1] and (ar[j[0]]+ar[j[1]])%k==0:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
