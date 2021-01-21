#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total_bribes = 0
    swaps = 1
    
    for index, item in enumerate(q):
        if item > index + 3:
            print("Too chaotic")
            return

    
    while (swaps != 0):
        swaps = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                swaps += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                total_bribes += 1
    print(total_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
