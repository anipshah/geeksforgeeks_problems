def spiral_matrix(x, r, c):
    # r is len of row
    # c is len of col
    # starting index for row
    p = 0
    # starting index for col
    q = 0

    while p < c and q < r:
        for i in range(q, r):
            print(x[p][i])
        p += 1

        for i in range(p, c):
            print(x[i][r - 1])
        r -= 1
        if q < r:
            for i in range(r - 1, q - 1, -1):
                print(x[c - 1][i])
            c -= 1

        if p < c:
            for i in range(c - 1, p - 1, -1):
                print(x[i][q])
            q += 1


first_matrix = [[1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7]]

len_row = len(first_matrix[0])
len_col = len(first_matrix)
spiral_matrix(first_matrix, len_row, len_col)
# second example
print("Second Example:")
second_matrix = [[1, 2, 3, 4, 5], [15, 16, 17, 18, 6], [14, 21, 20, 19, 7], [13, 12, 11, 10, 9, 8]]
len_row_sec = len(second_matrix[0])
len_col_sec = len(second_matrix)
spiral_matrix(second_matrix, len_row_sec, len_col_sec)
