def getmindiff(arr,k):
    temp = []
    n = len(arr)
    if n==1:
        return 0
    for i in range(n):
        if arr[i] <= 6:
            temp.append(arr[i]+k)
        else:
            temp.append(arr[i]-k)

    temp = sorted(temp)
    ans = temp[-1]-temp[0]
    return ans
    
    
arr=[1, 10, 14, 14, 14, 15]
k=6
print(getmindiff(arr,k)) #5
