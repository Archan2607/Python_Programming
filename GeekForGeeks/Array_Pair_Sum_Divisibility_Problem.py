"""
Question Link: - https://practice.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem/0

"""
#code

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    res={}
    if(n%2!=0):
        print("False")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if((a[i]+a[j])%k==0 and j not in res):
                    res[i]=a[i]
                    res[j]=a[j]
        if(len(res)==n):
            print("True")
        else:
            print("False")
        
    
    
