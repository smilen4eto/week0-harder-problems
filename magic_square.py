def magic_square(matrix):
    matlen = len(matrix)
    r_sum = [sum(x) for x in matrix]
    c_sum = [sum(x) for x in zip(*matrix)]
    d_l_sum = sum(matrix[i][i] for i in range(0, matlen))
    d_r_sum = sum(matrix[matlen-1-i][i] for i in range(matlen-1, -1, -1))
    if r_sum != c_sum or d_l_sum != d_r_sum:
        return False
    else:
        return True

print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
