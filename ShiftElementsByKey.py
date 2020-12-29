# shift elements by given key in matrix

def shift(mat,k):
    n=len(mat)
    if k > n:
        return
    i = 0
    
    while i < n:
        for j in range(k,n):
            print(mat[i][j], end= " ")
        for j in range(0,k):
            print(mat[i][j], end= " ")
        print(" ")
        i+=1
        
mat = [[1, 2, 3, 4], 
       [5, 6, 7, 8], 
       [9, 10, 11, 12], 
       [13, 14, 15, 16]] 
       
k=3
shift(mat,k)
