rows, cols = [int(x) for x in input().split()]

start_char = ord('a')

for row in range(rows):
    for col in range(cols):
        print(f"{chr(start_char + row)}{chr(start_char + row + col)}{chr(start_char + row)}", end=' ')
    print()

