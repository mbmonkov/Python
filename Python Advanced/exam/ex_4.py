def is_inside(matrix_size, r, c):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


def move_ship(matrix, row, col, command):
    matrix[row][col] = '-'
    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    if not is_inside(len(matrix), row, col):
        if row == -1:
            row = len(matrix) - 1
        elif row == len(matrix):
            row = 0
        if col == -1:
            col = len(matrix) - 1
        elif col == len(matrix):
            col = 0

    return row, col

n = int(input())

matrix = []
total = 0
position = None



for row_index in range(n):
    row_data = list(input())
    if 'S' in row_data:
        col_index = row_data.index("S")
        position = [row_index, col_index]
    matrix.append(row_data)


direction = input()
while direction != "collect the nets":
    current_row, current_col = position
    row_to_go, col_to_go = direction_mapper[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    #if  is_not_in_area(desired_row, desired_col, matrix):
    if desired_row < 0:
        desired_row = len(matrix) - 1
        continue
    elif desired_row > len(matrix):
        desired_row = 0
        continue
    elif desired_col < 0:
        desired_col = len(matrix) - 1
        continue
    elif desired_col > len(matrix):
        desired_col = 0
        continue

    if matrix[desired_row][desired_col] == "W":
        matrix[desired_row][desired_col] = "S"
        matrix[current_row][current_col] = "-"
        position = [desired_row, desired_col]
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: {position}")
        break

    elif matrix[desired_row][desired_col] != "-":
        matrix[desired_row][desired_col] = "S"
        matrix[current_row][current_col] = "-"
        total += int(matrix[desired_row][desired_col])
        position = [desired_row, desired_col]


    elif matrix[desired_row][desired_col] == "-":
        direction = input()
        continue


    direction = input()

if direction == "collect the nets":
    if total >= 20:
        print("Success! You managed to reach the quota!")
        print(f"Amount of fish caught: {total} tons.")
    else:
        print("You didn't catch enough fish and didn't reach the quota!")
        print(f"You need {20 - int(total)} tons of fish more.")
        print(f"Amount of fish caught: {total} tons.")