n = int(input())

flatten = []

for _ in range(n):
    elements = [int(el) for el in input().split(", ")]
    for el in elements:
        flatten.append(el)
print(flatten)
