def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("lets do some math w. functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# a puzz for extra credit, type it in anyway
print("here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 0.5))))

print("that becomes: ", what, "can you do it by hand?")
