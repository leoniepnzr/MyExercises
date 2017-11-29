#escape quotes with \ for when you use several double-quotes in one string e.g.

#variables to print out

#\t shoves the text in
tabby_cat = "\tI'm tabbed in."
#\n new line character
persian_cat = "I'm split\non a line."
#\\ will be \, way of writing out backslash, maybe important for no confusion
backslash_cat = "I'm \\ a \\ cat."

#""" is a multi-line character
#\t* makes a list
#line 19 with implemented new line character
#""" or "' depends on style
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

#prints out
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
