# Ceiling in a sorted array
"""
For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array

https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
"""


def ceiling_sorted_array(arr, x):

    n = len(arr)

    if x <= arr[0]:
        return 0

    for i in range(0, n):
        if arr[i] == x:
            return i
        if arr[i+1] >= x and arr[i] < x:
            return i+1
    return -1


arr = [1, 2, 8, 10, 10, 12, 19]
key = 0
ans = ceiling_sorted_array(arr, key)

if ans == -1:
    print("Not")
else:
    print(arr[ans])
