class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() #using super() gets you the old fxn
        #does this let you use fxn from multiple inheritances?
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
