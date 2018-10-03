#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    inp = s.split(':')
    if 'PM' in inp[2]:
        inp[0]=int(inp[0])+12
        inp[0]=str(inp[0])
        if inp[0]=='24':
            inp[0]='12'
    elif 'AM' in inp[2]:
        if inp[0]=='12':
            inp[0]='00'
    res = ':'.join(inp)
    res = res.rstrip('APM')
    
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
