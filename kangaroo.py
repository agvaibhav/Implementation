#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    loc1 = x1
    loc2 = x2
    if x2<x1:
        while(loc2<loc1 and v2>v1):
            loc1 = loc1+v1
            loc2 = loc2+v2
            if loc1 == loc2:
                return("YES")
                break
        return "NO"
    elif x1<x2:
        while(loc1<loc2 and v1>v2):
            loc1=loc1+v1
            loc2 = loc2+v2
            if loc1 == loc2:
                return("YES")
                break
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
