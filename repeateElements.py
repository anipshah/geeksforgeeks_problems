# Find the two repeating elements in a given array

def rep_ele(arr,array_size, number):
    if array_size == number + 2:
        for i in range(0, array_size-1):
            if arr[i] == arr[i+1]:
                print(arr[i])
    else:
        print("Invalid")

a = [4,4,5,3,2,2]
temp = sorted(a)
s=len(temp)
rep_ele(temp,s,4)
