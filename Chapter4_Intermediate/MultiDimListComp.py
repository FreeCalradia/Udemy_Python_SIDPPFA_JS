num_rows = 3
num_cols = 2

matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]  # die range gibt anzahl rows und cols, nicht lst vals
# klammern - je mehr etwas außerhalb steht, desto höherrangiger ist es. zb enthalten die rows cols
print(matrix)

matrix_2 = [[(i * num_cols + j) + 1 for j in range(num_cols)] for i in range(num_rows)]
print(matrix_2)

matrix[0][0] = 100  # ändert die liste , in den klammern row, col
print(matrix)
