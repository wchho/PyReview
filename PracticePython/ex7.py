# Ex7: taking only even elements of a list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f"this is a: \n{a}")

b = [a[x * 2 + 1] for x in range(0,int(len(a)/2))]
print(f"these are the even-th terms in a: \n{b}")

c = [number for number in a if number % 2 == 0]
print(f"these are the even terms in a: \n{c}")
