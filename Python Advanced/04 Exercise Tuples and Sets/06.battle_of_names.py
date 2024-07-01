n = int(input())

odd_set = set()
even_set = set()

for m in range(1, n + 1):
    name = input()
    ascii_value_of_name = sum(ord(char) for char in name) // m

    if ascii_value_of_name % 2 == 0:
        even_set.add(ascii_value_of_name)
    else:
        odd_set.add(ascii_value_of_name)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = even_set.symmetric_difference(odd_set)

print(', '.join(str(x) for x in result))