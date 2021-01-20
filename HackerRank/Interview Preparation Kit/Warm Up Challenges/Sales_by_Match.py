#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=0
    match=[]
    freq=[]
    pair=[]
    for i in ar:
        if i not in match:
            match.append(i)
    m=len(match)
    for i in range(m):
        freq.append(0)
    for i in range(m):
        pair.append(0)
    sell_sock=[]
    for i in range(n):
        for j in range(m):
            if ar[i] == match[j]:
                freq[j]=freq[j]+1
                if freq[j] == 2:
                    pair[j]=pair[j]+1
                    freq[j]=0
            
    return sum(pair)    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
