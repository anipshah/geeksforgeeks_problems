#Sorting array with reverse around middle

"""
Input : arr[] = {1, 6, 3, 4, 5, 2, 7}
Output : Yes
We can choose sub-array[3, 4, 5] on
reversing this we get [1, 6, 5, 4, 3, 2, 7]
again on selecting [6, 5, 4, 3, 2] and
reversing this one we get [1, 2, 3, 4, 5, 6, 7]
which is sorted at last thus it is possible
to sort on multiple reverse operation.

Input : arr[] = {1, 6, 3, 4, 5, 7, 2}
Output : No

https://www.geeksforgeeks.org/sorting-array-reverse-around-middle/
"""
def sorting_array_reverse_around_middle(arr,n):
    cp=arr
    for i in range(n):
        if not arr[i]==cp[i] and not arr[n-1-i]==cp[i]:
            return False
    return True

a=[1, 6, 3, 4, 5, 7, 2]
print(sorting_array_reverse_around_middle(a,len(a)))
