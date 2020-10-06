#Minimum sum of absolute difference of pairs of two arrays

"""
Input :  a[] = {3, 2, 1}
         b[] = {2, 1, 3}
Output : 0

Input :  n = 4
         a[] = {4, 1, 8, 7}
         b[] = {2, 3, 6, 5}
Output : 6

https://www.geeksforgeeks.org/minimum-sum-absolute-difference-pairs-two-arrays/
"""

def min_sum(a,b):
    a.sort()
    b.sort()
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i]-b[i])
    return sum


a = [4, 1, 8, 7]
b = [2, 3, 6, 5]
print(min_sum(a,b))
