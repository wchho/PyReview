a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(f"Here is your list: {a}")

a_comp = a < 5
print(a_comp)

lim_value = int(input("Enter the cut-off value: "))
a_new = []
for x in a:
    if x < lim_value:
        a_new.insert(1,x)

print(a_new)
