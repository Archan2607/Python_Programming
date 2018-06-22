"""

Question Link: - https://practice.geeksforgeeks.org/problems/find-nth-root-of-m/0


"""


#code
import math

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    p=math.ceil(m**(1/n))
    q=math.floor(m**(1/n))
    if p ** n == m:
        print(p)
    elif q ** n == m:
        print(q)
    else:
        print(-1)
