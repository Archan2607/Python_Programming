#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n=len(a)
    a1=[]
    for i in range(n):
        if i>=d:
            a1.append(a[i])
            a[i]=0
    for i in range(n):
        if a[i]!=0:
            a1.append(a[i])    
    return a1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
