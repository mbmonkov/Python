rows, columns = [int(x) for x in input().split(', ')]

matrix = []

max_sum = 0
current_matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] + matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            current_matrix =[
                [matrix[row_index][col_index], matrix[row_index][col_index + 1]],
                [matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]
            ]

print(*current_matrix[0])
print(*current_matrix[1])
print(max_sum)

