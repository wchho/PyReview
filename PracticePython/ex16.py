# Ex16: Simple password generator

import random
import string

def get_pw_length(default = "How long would you like your password?\n"):
    return int(input(default))

def password_gen(pw_len):
    char_bank = string.ascii_letters + string.digits + string.punctuation
    newPw = []
    for x in range(pw_len):
        newPw.append(char_bank[random.randint(0,len(char_bank)-1)])
    newPw = ''.join(newPw)
    return newPw


MyPass = password_gen(get_pw_length())
print(f"Here is your new password:\n{MyPass}")
