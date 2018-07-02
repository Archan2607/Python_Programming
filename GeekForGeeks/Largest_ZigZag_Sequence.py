"""

Question Link: - https://practice.geeksforgeeks.org/problems/largest-zigzag-sequence/0

"""
def larZigZagSumInMatrix(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == n-1:
        dp[i][j] = a[i*n+j]
        return dp[i][j]
    zzs = 0
    for k in range(n):
        if k!=j:
            zzs = max(zzs,larZigZagSumInMatrix(i+1,k))
    dp[i][j] = zzs+a[i*n+j]
    return dp[i][j]
def result():
    global a,n
    res = 0
    for i in range(n):
        res = max(res,larZigZagSumInMatrix(0,i))
        # for j in dp:
        #     print(j)
    print(res)
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    dp = [[-1 for i in range(n)] for j in range(n)]
    (result())
