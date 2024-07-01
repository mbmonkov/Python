def find_position(symbol, matrix):
    for row in range(len(matrix)):
        if symbol in matrix[row]:
            return [row, matrix[row].index(symbol)]


row = int(input())
matrix = [[x for x in input()] for _ in range(row)]

my_position = find_position("S", matrix)
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tons = 0
flag = False
while True:
    command = input()
    if command == "collect the nets":
        break

    matrix[my_position[0]][my_position[1]] = '-'
    current_row = my_position[0] + directions[command][0]
    current_col = my_position[1] + directions[command][1]

    if current_row not in range(len(matrix)):
        current_row = len(matrix) - 1 if current_row < 0 else 0
    elif current_col not in range(len(matrix[0])):
        current_col = len(matrix[0]) - 1 if current_col < 0 else 0

    if matrix[current_row][current_col] == "W":
        matrix[current_row][current_col] = "S"
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{current_row},{current_col}]")
        flag = True
        break

    elif matrix[current_row][current_col].isdigit():
        tons += int(matrix[current_row][current_col])

    matrix[current_row][current_col] = "S"
    my_position = [current_row, current_col]


if not flag:
    if tons >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - tons} tons of fish more.")
    if tons:
        print(f"Amount of fish caught: {tons} tons.")
    [print(''.join(x)) for x in matrix]






