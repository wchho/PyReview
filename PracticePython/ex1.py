# Ex1
import datetime

now = datetime.datetime.now()

name = input("What is your name? ")
age = input("What is your age? ")

yearsTill = 100 - int(age);
yearAt100 = int(now.year) + yearsTill;

print(f"Hello {name}, you will turn 100 in the year {yearAt100}.")
