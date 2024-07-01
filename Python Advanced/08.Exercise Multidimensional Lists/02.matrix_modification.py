rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    command = command.split()
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print('Invalid coordinates')

    elif command[0] == 'Add':
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value
    command = input()

for row in matrix:
    print(*row, sep=" ")