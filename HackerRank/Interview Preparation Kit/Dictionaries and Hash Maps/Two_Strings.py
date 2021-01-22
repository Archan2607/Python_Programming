#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    a=Counter(s1)
    b=Counter(s2)
    k=a&b
    
    return k

if __name__ == '__main__':
    
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        if(result):
            print("YES")
        else:
            print("NO")
            
