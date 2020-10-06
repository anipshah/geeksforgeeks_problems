def tiling_problem(n):
    if n<1:
        return 0
    if n<2:
        return 1
    if n==2:
        return 2

    return tiling_problem(n-1)+tiling_problem(n-2)

print(tiling_problem(4))

def tiling_problem_dy(n):
    count=[]
    for i in range(n+2):
        count.append(0)
    count[0]=0

    for i in range(1, n + 1):
        if (i > 2):
            count[i] = count[i - 1] + count[i - 2]

        elif (i < 2 or i == 1):
            count[i] = 1

        else:
            count[i] = 2

    return count[n]


print(tiling_problem_dy(7))
