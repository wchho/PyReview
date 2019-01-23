# Ex12: list ends
import random

a = list(random.sample(range(30),random.randint(3,18)))
print(a)

def get_ends(MyList):
    ends = [MyList[x] for x in range(0,len(MyList)) if x == 0 or x == len(MyList)-1]
    return ends

print(get_ends(a))
