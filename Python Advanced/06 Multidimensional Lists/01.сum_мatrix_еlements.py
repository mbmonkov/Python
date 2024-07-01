data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []
sum_nums = 0

for row_index in range(rows):
    elements = [int(x) for x in input().split(', ')]
    sum_nums += sum(elements)
    matrix.append(elements)

print(sum_nums)
print(matrix)