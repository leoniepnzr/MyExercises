# -*- coding: utf-8 -*-

from sys import exit
from random import randint, shuffle, choice
from math import sqrt
import time
import operator

class Scene(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Trapdoor(Scene):
    quips = [
        "I think you will have to live here forever.",
        "We both know how this is gonna end without food and drinks.",
        "Happy death!"
    ]

    def enter(self):
        print Trapdoor.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Mathroom(Scene):
    def enter(self):
        print "Welcome back to another awesome maze game."
        print "Another game, another lonesome house: You find yourself in the middle"
        print "of one big room full of numbers. Numbers on the ceiling, numbers"
        print "on the floor, furniture made out of numbers. What's happening here?"
        print "May I introduce: The Villa Of Math, or - even better - the Villa Of Death."
        print "\n"
        print "You are not a math expert? Poor you, this maze will end up deadly for you."
        print "But let's get started first:"
        print "The room you are standing in makes you feel pretty uncomfortable,"
        print "so you decide to take one door leading to another room."
        print "There are three doors to three rooms, which door do you take?"
        print "Room number \"1\", number \"2\", or number \"84251\"?"

        action = raw_input("> ")

        if action == "1":
            print "Behind the door is a trap door. You fall and end up buried"
            print "underneath math operators."
            print ""
            return 'trapdoor'

        elif action == "2":
            def print_welcome():
                print "The door closes behind you and happens to be locked. There is"
                print "no other door. And as you try to find an exit, you notice that"
                print "the walls are getting closer and closer. They will smash you."
                print "But there is a small screen that says"
                print "------ Welcome. Let's play a game *Jigsawstyle* ------"
                print "Good luck solving the math equations as fast as possible."
                print "Otherwise you will end up dead."
                time.sleep(5)
            ### -> bug! will not be executed
            start_time = 0
            actual_time = 0
            estimated_time = 0

            mathproblems = []

            while len(mathproblems) <= 1:
              mathproblems = [randint(1, n + 1) for n in range(1, randint(1, 9) + 1)]

            operations = ["+", "-", "*", "/"]

            def randomize_lists():
              shuffle(mathproblems)

            def is_number(s):
              try:
            	float(s)
            	return True
              except ValueError:
            	return False

            def ask_questions(p = []):
              num_of_questions_asked = 0
              correct_answers = 0
              min_questions_asked = sqrt(len(p))

              while len(p) > 1 or correct_answers < min_questions_asked:
            	first_number = choice(p)
            	second_number = choice(p)

            	operation = choice(operations)

            	print "%s %s %s = ?" % (first_number, operation, second_number)
            	num_of_questions_asked += 1

            	answer = 0

            	if operation == "+":
            	  answer = operator.add(first_number, second_number)
            	elif operation == "-":
            	  answer = operator.sub(first_number, second_number)
            	elif operation == "*":
            	  answer = operator.mul(first_number, second_number)
            	elif operation == "/":
            	  answer = operator.div(first_number, second_number)
            	else:
            	  answer = operator.mod(first_number, second_number)

            	user_answer = raw_input("> ")

                while int(user_answer) is not answer:
            	  print "That is wrong! Think again!"
                  user_answer = raw_input("> ")

            	while not is_number(user_answer):
            	  print "That is not a number! Please enter a valid number."
            	  user_answer = raw_input("> ")

            	if int(user_answer) == answer:
            	  correct_answers += 1

            	p.remove(first_number)

              return num_of_questions_asked

            def play_game():

              start_time = time.time()

              print_welcome()
              randomize_lists()
              estimated_time = ask_questions(mathproblems) * 5
              actual_time = time.time() - start_time

              print "It took you %r seconds to get that done." % actual_time
              print "If you got over %r seconds, you died." % estimated_time

              if actual_time > estimated_time:
            	print "Wow! You are such a lame duck. You can't even solve those easy equations? Shame on you."
                print "You deserve nothing more than death. The walls are gonna smash you."
                return 'death'

              else:
            	print "You made it! A number 7 with wings is showing up and flies"
                print "away with you through the ceiling, breaking through a bunch"
                print "of 8, 5, 4 and 0 and takes you into the math-free freedom."
                return 'freedom'

            play_game()

        elif action == "84251":
            print "What a strange number, what do you think will be behind this door?"
            print "Again, the door closes behind you and is locked, no way to get out."
            print "You enter and find a small keypad in the middle of the room."
            return 'room84251'

        else:
            print "Type in one of the numbers you are seeing!"
            return 'mathroom'

class Room84251(Scene):
    def enter(self):
        print "The keypad tells you to enter 5 numbers."
        print "You have to enter the number of the room you are in, but backwards."
        print "Do you remember?"
        print "If you are wrong, you won't get through and slowly starve to death."
        print "Get it right, otherwise you will not make it!"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        code = ("15248")
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 1:
            print "Starving to death awaits you, that was wrong!"
        if guess == code:
            return 'death'

class Freedom(Scene):
    def enter(self):
        print "You fly away with the pretty number 7 and finally feel free again."
        print "Happy end!"
        exit(1)

class Death(Scene):
    def enter(self):
        print "The keypad beeps for a second, then the door behind you is opening"
        print "up again. Pretty frustrating finding yourself back in the same room,"
        print "isn't it? There must be another way out."
        print "But the search takes you too long, you die."
        exit(1)

class Map(object):
    scenes = {
    'mathroom': Mathroom(),
    'trapdoor': Trapdoor(),
    'room84251': Room84251(),
    'freedom': Freedom(),
    'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('mathroom')
a_game = Engine(a_map)
a_game.play()
