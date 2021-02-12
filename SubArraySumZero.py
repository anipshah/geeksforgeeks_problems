# Find if there is a subarray with 0 sum

def checksum(l):
    sub_list_sum = 0
    temp = set()
    for i in range(len(l)):
        sub_list_sum += l[i]
        print(temp)
        if sub_list_sum==0 or sub_list_sum in temp:
            return True
        temp.add(sub_list_sum)
    return False

l=[4, 2, -3, 1, 6]
print(checksum(l))
