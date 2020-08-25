def move_zeros_to_end(a):
    count = 0
    # non-zero elements goes first
    for i in range(len(a)):
        if a[i] != 0:
            a[count] = a[i]
            count += 1
    # add zeroes up to len of list
    while count < len(a):
        a[count] = 0
        count += 1
    return a


arr1 = [1, 0, 3, 4, 0, 0, 5]
new_array = move_zeros_to_end(arr1)
print(new_array)

