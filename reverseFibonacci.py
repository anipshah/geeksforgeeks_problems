def rev_Fibonacci(n):
    ans=[0]*n

    ans[0]=0
    ans[1]=1

    for i in range(2,n):
        ans[i]=ans[i-2]+ans[i-1]

    for i in range(n-1,-1,-1):
        print(ans[i], end= " ")


rev_Fibonacci(5)
