# Find common elements in three sorted arrays

def common(l1,l2,l3):
    n1=len(l1)
    n2=len(l2)
    n3=len(l3)
    
    i,j,k = 0,0,0
    res=[]
    while i<n1 and j<n2 and k<n3:
        if l1[i] == l2[j] and l2[j] == l3[k]:
            res.append(l1[i])
            i+=1
            j+=1
            k+=1
        elif l1[i]<l2[j]:
            i+=1
        elif l2[j]<l3[k]:
            j+=1
        else:
            k+=1
    return res
            
l1=[2,3,4,5]
l2=[1,2,3]
l3=[1,2,3,4,5,6,7]

print(common(l1,l2,l3)) # [2,3]
    
