def isPowerOfTwo(num):
    if num==0:
        return False
    else:
        while num%2==0:
            num/=2
        return (num==1)

print(isPowerOfTwo(64))
