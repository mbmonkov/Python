rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for r in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum = 0
    for row_index in range(rows):
        sum += matrix[row_index][col_index]
    print(sum)