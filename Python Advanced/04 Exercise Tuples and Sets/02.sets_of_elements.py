a, b = (int(x) for x in input().split())

a_set = set()
b_set = set()

for _ in range(a):
    a_set.add(input())

for _ in range(b):
    b_set.add(input())

print('\n'.join(a_set.intersection(b_set)))
