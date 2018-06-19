"""
Question Link : -

https://practice.geeksforgeeks.org/problems/probability-of-knight/0

Here in the GeeksForGeeks IDE it will give runtime error, so being on a safe side we can use the same logic to right the code in C/C++

I also have attached the same code file in C++



"""
#code

# Direction vector for the Knight
dx = [ 1, 2, 2, 1, -1, -2, -2, -1 ]
dy = [ 2, 1, -1, -2, -2, -1, 1, 2 ]
 
def inside(x, y):
 
    return (x >= 0 and x < N and y >= 0 and y < N)
 
# Bottom up approach for finding the 
# probability to go out of chessboard.
def findProb(start_x, start_y, steps):
 
    # dp array
    dp1 = [[[0 for i in range(N + 1)]
               for j in range(N + 1)]
               for k in range(N + 1)]
 
    # For 0 number of steps, each 
    # position will have probability 1
    for i in range(N):
         
        for j in range(N):
            dp1[i][j][0] = 1
 
    # for every number of steps s
    for s in range(1, steps + 1):
     
        # for every position (x,y) after
        # s number of steps
        for x in range(N):
             
            for y in range(N):
                prob = 0.0
 
                # For every position reachable from (x,y)
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
 
                    # if this position lie inside the board
                    if (inside(nx, ny)):
                        prob += dp1[nx][ny][s-1] / 8.0
                 
                # store the result
                dp1[x][y][s] = prob
             
    # return the result
    return dp1[start_x][start_y][steps]
 

t = int(input())
for _ in range(t):
    N,x,y,k = list(map(int,input().split()))
    #print(findProb(x,y,k))
    
