#inheritance vs. composition
#used to indicate that one class will get most functions from parent class
#e.g. class Foo(Bar) -> make a class Foo that inherits from Bar
#imply, override or alter o the parent

#implicit inheritance (implicit)
#defining function in parent but NOT in child
#pass = new block, creates class with nothing more to define in it
#if putting functions in base class, all subclasses will get features

#override explicitly (override)
#when child should behave differently
#parent object child parent -> behaves differently

#alter before or after (altered)
#super for parent version to call
#alter behavior befor or after execution
#overriden thing runs, then altering with super

class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


#reason for super:
#multiple inheritance = defining a class that inherits from one or more classes
#to do: method resolution order and C3 algorithm - connected in super(), Python will find right function

#super() with __init__: most common use of super = init in base classes

#composition: other way of inheritance is simply using classes and modules

class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

#no parent child is-a relationship, therefore no Parent()
#has-a realtionship, Child has a Other

#when to use inheritance and composition:
#duplicated code: inheritance solves by implying features in base class, composition by modules
#guidelines when to use what: avoid multiple inheritance, composition to pack codes in modules
#inheritance only when clearly related pieces of reusable code exist (in one single common conceot)

#OOP = social convention that programmers invented to package and share code
