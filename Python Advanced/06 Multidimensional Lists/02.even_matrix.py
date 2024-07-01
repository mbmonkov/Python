rows = int(input())

matrix = []

for row_index in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

even_matrix = []

for row_index in range(rows):
    even_matrix.append([])
    for col_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][col_index]
        if current_element % 2 == 0:
            even_matrix[row_index].append(current_element)

print(even_matrix)