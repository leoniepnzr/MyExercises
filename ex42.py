#fish class, salmon class, Mary object, salmon salar = class with more attributes, becomes object when looking at instance
#Mary is a kind of salmon that is kind of fish -> object is a class is a class

#is-a = when talking about objects and classes being related by class relationship
#has-a = being related because they reference

#Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is-a Animal is-a object
class Dog(Animal):

    def __init__(self, name):
        ##self has-a name
        self.name = name

##
class Cat(Animal):

    def __init__(self, name):
        ##self has-a name
        self.name = name

##
class Person(object):

    def __init__(self, name):
        ##self has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##
class Employee(Person):

    def __init__(self, name, salary):
        ##__init__ indicates parent class reliably
        super(Employee, self).__init__(name)
        ##self has-a salary
        self.salary = salary

##class Fish has-a function called pass
class Fish(object):
    pass

##class Salmon has-a function called pass
class Salmon(Fish):
    pass

##class Halibut has-a function called pass
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

##mary has-a pet satan, satan is-a Cat
mary.pet = satan

## frank is-a Employee with the attributes Frank as name and 120000 as salary
frank = Employee("Frank", 120000)

##frank has-a pet rover, rover is-a Dog
frank.pet = rover

##flipper is-a instance of class Fish
flipper = Fish()

##crouse is-a instance of class Salmon
crouse = Salmon()

##harry is-a instance of class Halibut
harry = Halibut()
