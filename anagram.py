def ar(words):
    d = {}
    new=[]
    for i in words:
        temp = ''.join(sorted(i))
        if temp not in d:
            d[temp] = [i]
        else:
            d[temp].append(i)
    print(d)

    for i in d.values():
        new.append(i)
    return new


words=['cat','dog','tac','god','act']
x = ar(words)
print(x)
