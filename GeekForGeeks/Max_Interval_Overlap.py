"""

Problem Link: - https://practice.geeksforgeeks.org/problems/maximum-intervals-overlap/0



"""
from collections import Counter

def algo(starts, ends):
    times = sorted(set(start + end))
    c = 0
    max_c = 0
    max_t = None
    
    starts_by_time = Counter(starts)
    ends_by_time = Counter(e + 1 for e in ends)
    
    for t in times:
        c = c + starts_by_time[t] - ends_by_time[t]
        if c > max_c:
            max_c = c
            max_t = t
            
        max_c = max(max_c, c)
    
    return max_c, max_t

T = int(input())
res = []
for i in range(T):
    k = int(input())
    start = [int(x) for x in input().split()]
    end = [int(x) for x in input().split()]

    print(' '.join(str(n) for n in algo(start, end)))
