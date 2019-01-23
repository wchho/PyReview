# Ex15: reversing word order

def get_string(default = "Enter a string: \n"):
    return str(input(default))

def reverse_word_order(a_string):
    return ' '.join(a_string.split()[::-1])

MyString = get_string()
print(reverse_word_order(MyString))
