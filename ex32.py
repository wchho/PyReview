the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#first for loop
for number in the_count:
    print(f"This is the count {number}")

#same as above
for fruit in fruits:
    print(f"this is the fruit: {fruit}")

#for a mixed list
for i in change:
    print(f"i got {i}")

#here's how to build lists
elements = []

for i in range(0,6):
    print(f"adding {i} to the list")
    elements.append(i)

#now we print
for i in elements:
    print(f"element was: {i}")
