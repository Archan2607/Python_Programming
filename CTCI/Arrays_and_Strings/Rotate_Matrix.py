"""

Rotate a matrix by 90 degreees

"""
def rotateMatrix(mat):
     
    # Consider all squares one by one
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):
            # store current cell in temp variable
            temp = mat[x][y]
 
            # move values from right to top
            mat[x][y] = mat[y][N-1-x]
 
            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
 
            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
 
            # assign temp to left
            mat[N-1-y][x] = temp
 
 
def displayMatrix( mat ):
     
    for i in range(0, N):
         
        for j in range(0, N):
             
            print (mat[i][j], end = ' ')
        print ("")
     
     
N=int(input()) 
 
mat = [[int(input()) for x in range(N)] for y in range(N)]
 
displayMatrix(mat)

print("")
rotateMatrix(mat)
 
# Print rotated matrix
displayMatrix(mat)
 
 
