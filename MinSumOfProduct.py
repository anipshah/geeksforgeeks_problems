def min_sum(l1,l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    res = 0
    n1 = len(l1)
    n2 = len(l2)
    
    if n1 != n2:
        return
    
    for i in range(n):
        res += (l1[i]*l2[n-i-1])
    
    return res
    
A = [3, 1, 1] 
B = [6, 5, 4] 

print(min_sum(A,B)) #23
