# Ex10: list overlaps
import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(30),random.randint(5,20))
b = random.sample(range(30),random.randint(5,20))

print(f"Here is a:\n{a}")
print(f"Here is b:\n{b}")

c = [x for x in a if x in b]
print(f"Here is the overlap:\n{c}")
