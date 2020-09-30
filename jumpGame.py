def jump_game(arr):
    n = len(arr)
    jump = 0
    for i in range(n):
        if i > jump:
            return False
        jump = max(jump, i + arr[i])
    return True

arr=[1,3,0,1,2]
print(jump_game(arr))
