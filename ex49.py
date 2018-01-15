#to turn tuples list into Sentence object, four tools
#   way to loop through list of scanned words
#   matching different types of tuples expected in Subject Verb Object
#   way to peek at a tuple, making decisions
#   skipping things we don't need, kind of stop words
#   Sentence objects for putting results in it

#peek function to look at next element in tuple list, match function to take off and work with it

#the sentence grammar:
#   in parser we want to produce Sentence object with three attributes:
#       Sentence.subject - subject, could default to "player" (piece of every subject) -> will be a noun
#       Sentence.verb - action of sentence, verb
#       Sentence.object - noun, what the verb is done on, e.g. "run north" -> object = north
#-> parser -> use functions, convert scanned sentence into a List of Sentence objects to match input

#a word on exceptions:
#exception raising with ParserError -> classes to give it the type of Exception
#use of raise keyword to raise exception

#the parser code: in Repositories from here on
