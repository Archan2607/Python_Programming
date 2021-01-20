#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if s=='a':
        return n
    m=len(s)
    value=0
    count=0
    a=0
    value=n//m
    for i in s:
        if i =='a':
            a=a+1
    value1=value*a
    k=value*m
    rem_a=0
    rem=n-k
    if rem==0:
        return value1
    else:
        for i in range(rem):
            if s[i] =='a':
                rem_a=rem_a+1   
        value1=value1+rem_a
        return value1 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
