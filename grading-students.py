#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    res=[]
    for i in grades:
        if i>=38:
            if (((int(i/5)+1)*5)-i)<=2:
                res.append((int(i/5)+1)*5)
            else:
                res.append(i)
        else:
            res.append(i)
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
