people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we shouldn't take the cars")
else:
    print("we can't decide")

if trucks > cars:
    print("too many trucks")
elif trucks < cars:
    print("maybe we could take the trucks")
else:
    print("we still can't decide")

if people > trucks:
    print("alright, let's just take the trucks")
else:
    print("fine let's stay home")

    
