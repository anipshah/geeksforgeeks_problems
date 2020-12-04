# First element occurring k times in an array

def ktimes(l,k):
    """
    :param l: array of numbers
    :param k: key
    :return: first element occurring k times in array
    """
    count_dic={}
    for i in range(len(l)):
        if l[i] in count_dic:
            count_dic[l[i]]+=1
        else:
            count_dic[l[i]]=1

    for i in range(len(l)):
        if count_dic[l[i]]==k:
            return l[i]
    return -1

print(ktimes([1,2,1,3,4,4,4],3)) # 4
print(ktimes([1,2,1,3,4,4,4],4)) # -1
