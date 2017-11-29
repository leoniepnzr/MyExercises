# -*- coding: utf-8 -*-
name = 'Leonie Panzer'
age = 23
height = 74 % 100 * 2.54 #cm
weight = 180 % 100 * 0.45 #kg
eyes = 'Brown'
teeth = 'White'
hair = 'Blonde'

print "Let's talk about %s." % name
print "She's %d cm tall." % height
print "She's %d kg heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
