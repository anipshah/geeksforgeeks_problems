def max_subarray(l):
    max_sofar=l[0]
    max_ending=l[0]

    for i in range(1,len(l)):
        max_ending = max(max_ending+l[i],l[i])
        max_sofar = max(max_ending,max_sofar)
    return max_sofar

print(max_subarray([1,3,-1,-10,10,-30,20,60])) # 80
