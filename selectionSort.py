arr = [10, 56, 2, 5, 90]
# from 0th index to last index
for i in range(0, len(arr)):

    index = i
    # compare with other values
    for j in range(i+1, len(arr)):
        if arr[index] > arr[j]:
            index = j
    # swap values
    arr[i], arr[index] = arr[index], arr[i]

for i in range(len(arr)):
    print(arr[i])