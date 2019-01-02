ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list, let's fix it")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("there we go: ", stuff)

print("let's do some things with stuff.")

print(stuff[1]) # second item
print(stuff[-1]) # last item?
print(stuff.pop()) #what does pop do? removes last item
print(' '.join(stuff))
print('#'.join(stuff[3:6])) # ranges in python don't include final idx
