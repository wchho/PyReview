# Ex6: Palindrome detector

string = str(input("Enter a string to test if it's a palindrome: "))

trueStorage = False
#while trueStorage == False:
#    for x in string:
for x in list(range(0,len(string))):
    if string[x] != string[-x-1]:
        trueStorage = False
    else:
        trueStorage = True
#        print(f"{string[x]}, {string[-x-1]}")

if trueStorage == True:
    print(f"{string} is a palindrome!!")
if trueStorage == False:
    print(f"{string} is not a palindrome :(")

# there is a quicker way to do this...
# taking the string, reversing it, and...
# conducting a str1 == str2 comparison
