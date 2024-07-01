rows = int(input())

matrix = []
primary_diagonal = 0

for r in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for row_index in range(rows):
    primary_diagonal += matrix[row_index][row_index]

print(primary_diagonal)

