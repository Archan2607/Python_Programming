#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    newq=Counter()
    new=Counter()
    count=0
    for op,val in queries:
        if op==1:
            newq[new[val]]-=1
            new[val]+=1
            newq[new[val]]+=1
        elif op==2:
            if new[val]>0:
                newq[new[val]]-=1
                new[val]-=1
                newq[new[val]]+=1
        else:
            if newq[val]>0:
                print("1")
            else:
                print("0")
            
            
                

if __name__ == '__main__':
    
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
