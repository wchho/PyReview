#Ex4

number = int(input("Enter a number to find divisors: "))

potential = list(range(1,int(number/2)+1))
print(potential)
divisors = []
for x in potential:
    if number % x == 0:
        divisors.append(x)

divisors.append(number)
print(f"Your divisors are: {divisors}")
