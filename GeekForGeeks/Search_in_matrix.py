"""

Question Link: - https://practice.geeksforgeeks.org/problems/search-in-a-matrix/0

"""

t=int(input())

for i in range(t):
    temp=list(map(int,input().split()))
    ele=list(map(int,input().split()))
    k=int(input())
    ele=set(ele)
    print(1) if k in ele else print(0)
        
            
            
