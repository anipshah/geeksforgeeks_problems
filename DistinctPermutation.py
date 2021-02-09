def cal_fact(n):
    fact=1
    for i in range(2,n+1):
        fact *=i
    return fact
    
def fact(s):
    temp={}
    for i in s:
        if i not in temp:
            temp[i]=1
        else:
            temp[i]+=1
    print(temp)
    n=len(s)
    div =1 
    for key, value in temp.items():
        div *= cal_fact(value)
    up = cal_fact(n)
    if div != 0:
        ans = up / div
    else:
        ans=0
    return int(ans)

print(fact("aab"))
