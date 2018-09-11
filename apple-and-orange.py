#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap=[]
    orange=[]
    for i in apples:
        ap.append(a+i)
    for j in oranges:
        orange.append(b+j)
    count = 0
    for k in ap:
        if k<=t and k>=s:
            count+=1
    print(count)
    countor = 0
    for l in orange:
        if l<=t and l>=s:
            countor+=1
    print(countor)
        
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
