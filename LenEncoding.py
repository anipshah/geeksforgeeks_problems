# Run Length Encoding in Python

def encoding(s):
    temp = {}
    for i in s:
        if i not in temp: 
            temp[i] = 1
        else:
            temp[i] += 1
    ans = ""
    for key, value in temp.items():
        ans = ans + str(key) + str(value)
    return ans

print(encoding("aasswwq"))  # a2s2w2q1
print(encoding("qqqqpppaaooo")) # q4p3a2o3
