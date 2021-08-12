
#to check if we can go to the particualr point
def issafe(arr,x,y,n):
    if x<n and y<n and arr[x][y]==1:
        return True
    return False
def ratinMaze(arr,x,y,n,solArr):
    #base case
    if x==n-1 and y==n-1:
        solArr[x][y]=1
        return True
    
    if issafe(arr,x,y,n):
        solArr[x][y]=1
        #checking if we can go to x+1
        if ratinMaze(arr,x+1,y,n,solArr):
            return True
        #else if we can go to the y+1
        if ratinMaze(arr,x,y+1,n,solArr):
            return True
        #backtrack
        solArr[x][y]=0
        return False

arr=[
    [1,0,1,0,1],
    [1,1,1,1,1],
    [0,1,0,1,0],
    [1,0,0,1,1],
    [1,1,1,0,1]
    ]
solArr=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]
    
ratinMaze(arr,0,0,5,solArr)
print(solArr)

# [[1, 0, 0, 0, 0], 
# [1, 1, 1, 1, 0], 
# [0, 0, 0, 1, 0], 
# [0, 0, 0, 1, 1], 
# [0, 0, 0, 0, 1]]
