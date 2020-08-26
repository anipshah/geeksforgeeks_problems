# This method print Longest increasing subsequence
def largest_subsequence(arr):
    current_max = 1
    max_count = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1] and max_count >= current_max:
            current_max += 1
        if current_max > max_count:
            max_count = current_max
    return max_count


a = [10, 2, 3,4,5,11,8]
print(largest_subsequence(a))
