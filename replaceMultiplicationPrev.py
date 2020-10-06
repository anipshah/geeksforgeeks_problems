# Replace every array element by multiplication of previous and next
'''
Input: arr[] = {2, 3, 4, 5, 6}
Output: arr[] = {6, 8, 15, 24, 30}

// We get the above output using following
// arr[] = {2*3, 2*4, 3*5, 4*6, 5*6}
https://www.geeksforgeeks.org/replace-every-array-element-by-multiplication-of-previous-and-next/
'''
arr=[2,3,4,5,6]

def replcae_multi_pre(a):
    n=len(a)
    if n<=1:
        return

    prev= a[0]
    a[0]=a[0]*a[1]

    for i in range(1, n-1):
        current= a[i]
        a[i]=prev*a[i+1]
        prev=current
    a[n-1]=prev*a[n-1]
    return a

print(replcae_multi_pre(arr))
