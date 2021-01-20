#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ftpr=open(os.environ['OUTPUT_PATH'],'w')
    total=0
    total_list=[]
    sum1=[]
    for i in range(6):
        for j in range(6):
            sum1.append(arr[i][j])
            
    #ftpr.write(str(sum1) + ' ')
    ftpr.close()
    sum2=len(sum1)
    for i in range(sum2):
        if(i<22):
            if(i>=0 and i<4):
                total=sum1[i]+sum1[i+1]+sum1[i+2]+sum1[i+7]+sum1[i+12]+sum1[i+13]+sum1[i+14]
                total_list.append(total)
                total=0
            if(i>=6 and i<10):
                total=sum1[i]+sum1[i+1]+sum1[i+2]+sum1[i+7]+sum1[i+12]+sum1[i+13]+sum1[i+14]
                total_list.append(total)
                total=0
            if(i>=12 and i<16):
                total=sum1[i]+sum1[i+1]+sum1[i+2]+sum1[i+7]+sum1[i+12]+sum1[i+13]+sum1[i+14]
                total_list.append(total)
                total=0
            if(i>=18 and i<22):
                total=sum1[i]+sum1[i+1]+sum1[i+2]+sum1[i+7]+sum1[i+12]+sum1[i+13]+sum1[i+14]
                total_list.append(total)
                total=0
                
    return max(total_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
