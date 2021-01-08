def getminmax(arr,k):
    n=len(arr)
    
    if n==1:
        return 0
    
    arr=sorted(arr)
    ans = arr[n-1] - arr[0] 
    max_diff= arr[n-1] - arr[0]
    min_diff = arr[0] + k
    
    if max_diff < min_diff:
        max_diff, min_diff = min_diff, max_diff
        
    for i in range(1, n-1):
        add = arr[i] + k
        sub = arr[i] - k
        
        if sub >= min_diff and add <= max_diff:
            continue
        
        if max_diff-sub <= add-min_diff:
            min_diff=sub
        else:
            max_diff=add
    return min(ans, max_diff-min_diff)
    
print(getminmax([4,2,5,9,0,1],4)) # 5
