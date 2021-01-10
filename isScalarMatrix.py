def isScalarMatrix(mat):
    if len(mat)!=len(mat[0]):
        return None
    n = len(mat)
    
    for i in range(n):
        for j in range(n):
            if i!=j and mat[i][j]!=0:
                return False
    for i in range(0,n-1):
            if mat[i][i]!=mat[i+1][i+1]:
                return False
    return True
    
arr=[[1,0,0],[0,1,0],[0,0,1]]
arr2=[[2,0,0],[1,2,3],[0,1,2]]
print(isScalarMatrix(arr)) # True
print(isScalarMatrix(arr2)) # False
