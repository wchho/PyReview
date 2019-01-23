# Ex11: prime number checker

def get_integer(default = "Give me a number: "):
    return int(input(default))

numInput = get_integer()

def check_prime(number):
    #number = int(input("Enter a number to find divisors: "))

    potential = list(range(1,int(number/2)+1))
    #print(potential)
    divisors = []
    for x in potential:
        if number % x == 0:
            divisors.append(x)

    divisors.append(number) #adding itself...

    if len(divisors) == 2: # it's prime
        return True
    else:
        return False

print(f"Is {numInput} a prime number? {check_prime(numInput)}")
