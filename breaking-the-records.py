#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxsc=0
    minsc=0
    maxj=scores[0]
    minj=scores[0]
    for i in scores:
        if i>maxj:
            maxsc+=1
            maxj=i
        elif i<minj:
            minsc+=1
            minj=i
    return("{}{}".format(maxsc,minsc))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
