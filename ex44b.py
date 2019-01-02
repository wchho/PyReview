class Parent(object):
    def override(self):
        print("PARENT override()")
    def basic(self):
            print("PARENT basic()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

dad.basic()
son.basic()
