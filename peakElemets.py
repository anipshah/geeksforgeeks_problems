def peak_element(arr):
    n=len(arr)
    i=0
    if n==1 or (arr[0]>=arr[1]):
        print(arr[0])
    if (arr[n-1]>=arr[n-2]):
        print(arr[n-1])

    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            print(arr[i])


ar=[10,20,15,2,23,90,67]
peak_element(ar)
