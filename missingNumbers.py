# This method find missing numbers in given list
def missing_numbers(array):
    missing_numbers_list = []
    # from 0th index number to last index number
    for i in range(array[0], array[-1]+1):
        if i not in array:
            missing_numbers_list.append(i)
    return missing_numbers_list


a = [1, 4, 5, 10, 7]
# sort list
b = sorted(a)
numbers = missing_numbers(b)
print(numbers)