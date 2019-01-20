# # Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ?? class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ?? class Dog has-a __init__ with params self, name
        self.name = name

## ?? class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ?? class Cat has-a __init__ with params self, name
        self.name = name

## ?? class Person is-a object
class Person(object):

    def __init__(self, name):
        ## ?? class Person has-a __init__ with params self, name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ?? class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ?? class Fish is-a object
class Fish(object):
    pass

## ?? class Salmon is-a Fish
class Salmon(Fish):
    pass

## ?? class Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a attribute pet, satan
mary.pet = satan

## Frank is-a Employee with params name: Frank, and salary: 120000
frank = Employee("Frank", 120000)

## Frank has-a attribute pet, rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
