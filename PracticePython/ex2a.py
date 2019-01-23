num = int(input("Enter a number: "))
check = int(input("Enter a number to check by: "))

if num % check == 0:
    print(f"{num} divides evenly by {check}!!")
else:
    print(f"Sorry, {num} is not divisible by {check}...")
