#advanced user input

#-> allow more words and not keeping it that strict

#building up a lexicon of 'allowed' words

#breaking up a sentence: sentences are words separated by phrases -> splitting sentences

#lexicon tuples: figuring out what type of word it is, using Python's tuple (unmodifyable list)
#raw input, carve it into words with split, analyse type, making sentence

#scanning input: writing scanner, takes input and returns sentence composed of tuples with (TOKEN; WORD) pairings
#if not in lexicon -> returning word but token is error

#exceptions and numbers: converting numbers with using exceptions (= error from some runned function, exception is "raised", you have to handle with it)
#e.g. int = "hell" -> no return since it's not an integer, ValueError exception -> you can deal with it
#dealing with "try" and "except": try: return int(s), except ValueError: return None
#code you want to try in try block, code to run for error in except

#test first challenge: writing automated test, THEN you write code -> when you can't figure out, how code is implemented
#but imaginable how to work with it
#create one small part of test
#make sure it runs and fails, so that is actually confirming something
#go to source file lexicon.py and write code that makes test pass

#other method of writing code: making skeleton-funciton, adding comments, code what comments describe, remove comments that are repeating
#called: pseudo-coding

#combined:
#   writing test that fails
#   fill skeleton with comments describing how it works
#   replace comments with code until passing
#   repeat

#try-except: only for handling exceptions, NEVER  to alternative if-else
