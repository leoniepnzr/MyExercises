#object oriented programming language, OOP

#modules are like dicts
mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

#this goes in mystuff.py
def apple():
    print "I AM APPLES!"

import mystuff
mystuff.apple()

def apple():
    print "I AM APPLES!"
tangerine = "Living reflection of a dream"

import mystuff

mystuff.apple()
print mystuff.tangerine

#different syntax
mystuff['apple'] #get apple from dict
mystuff.apple() #get apple from module
mystuff.tangerine #same thing, it's just a variable

#very common pattern: key=value style container, get something out with key's name
#for dicts: key = string ([key]), for modules: key = identifier (.key)

#classes are like modules

#objects are like import (mini-import)
 thing = MyStuff()
 thing.apple()
 print thing.tangerine
#Python looks for MyStuff(), sees that it's a class
#crafts empty object, with functions using def
#"magic" init function? -> calls that function to initialize new object
#extra variable self (new object), set variables on it
#self.tangerine as song lyrics, set it to thing variable to work with it
#NOT giving class, using blueprint for class
#classes are like blueprints or definitions for creating minimodules
#instantiation = how you make AND import, create object from class
#created mini-modules are objects -> variable to work with it

# dict style
mystuff[’apples’]
# module style
mystuff.apples()
print mystuff.tangerine
# class style
thing = MyStuff()
thing.apples()
print thing.tangerine
