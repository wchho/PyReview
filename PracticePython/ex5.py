#Ex5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

union_list = []

for x in list(set(a)):
    if x in list(set(b)):
        union_list.append(x)

print(a)
print(b)

#c = a.union(b)
print(union_list)
