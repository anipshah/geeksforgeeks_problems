# Number of local extrema in an array

def find(arr):
    ans=0
    for i in range(1, len(arr)-1):
        if arr[i] < arr[i+1] and arr[i] < arr[i-1]:
            ans+=1
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            ans+=1
    return ans
    

arr=[1,5,2,5,7]

print(find(arr))
