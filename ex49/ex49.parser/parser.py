#basic set
#exception we need for parser error, ParserError exception class you can throw
class ParserError(Exception):
    pass

#sentence Object
class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take (’noun’,’princess’) tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

#function that can peek on list and return kind of word, what kind of sentence are we dealing with (based on next word)?
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

#call another function to consume that word and carry on
#match function -> expected word is right type? taking off list and returns word
#need to peek to check what we are handling with, matching words afterwards to create sentence
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

#skipping words that aren't useful with stop word list (the, and, a..)
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
        #skip doesn't skip one word, as many as it finds

#parsing a verb, skipping stop words, peek to make sure next is verb, if not ParserError, if match to take off list
def parse_verb(word_list):
    skip(word_list, 'stop')
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

#sentence objects, skip stop words, peek, correct?, parse_object noun AND direction as possible objects, subjects similar again, hande player -> use peek
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

#final parse_sentence
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj, verb, obj)
