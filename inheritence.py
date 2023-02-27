
from test import Test

class Parent(Test):
    def display(self):
        print('This is parent')


class Child(Parent):
    def display(self):
        # super().display()   #same name 
        Parent.display(self)
        print('This is child')


child = Child()
child.sub(10,4)
child.display()
child.display()
child.add(2,8)

parent = Parent()

