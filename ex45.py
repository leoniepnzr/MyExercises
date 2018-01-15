# -*- coding: utf-8 -*-
from sys import exit
from random import randint
import time

class Engine(object): #game engine, how you move through game
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Scene(object): #for undefined scenes
    def enter(self):
        print "Excuse me?"
        exit(1)

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
            print "Behind the door is a trap door that looks like a big 0. You fall through and"
            print "end up buried underneath math operators."
            print "You died."
            return 'trapdoor'

        elif action == "2":
            print "The door closes behind you and happens to be locked. There is"
            print "no other door. And as you try to find an exit, you notice that"
            print "the walls are getting closer and closer. They will smash you."
            print "But there is a small screen that says"
            print "------ Welcome. Let's play a game *Jigsawstyle* ------"
            print "Good luck solving the following math equation."
            print "If you fail, you will end up dead."
            time.sleep(5) #sleeps so that you can read through instructions

            def ask_question():
                print "What is 6 / 2 * 3 + 8 / 2 + 11 - 7?"
                user_input = raw_input("> ")
                answer = int(user_input)

                if answer == 17:
                    print "True! Good job!"
                    return 'riddle'

                else:
                    print "That is wrong! You die!"
                    exit(1)

            ask_question()

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
        code = "%d%d%d%d%d" % (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))
        code = ("15248")
        guess = raw_input("[keypad]> ")

        if guess != code:
            print "Starving to death awaits you, that was wrong! Sorry."
            exit(1)
        if guess == code:
            return 'death'

class Riddle(Scene):
    def enter(self):
        print "A pretty number 7 with wings flies through the ceiling and lands right"
        print "next to your feet. Before you can get on its back, you need to solve a riddle:"
        print "What three positive numbers give the same result when multiplied and added together?"
        print "This is your door to freedom - so choose wisely!"
        answer = "%d, %d, %d" % (randint(1,9), randint(1,9), randint(1,9))
        answer = ("1, 2, 3")
        guess = raw_input("[keypad]> ")

        if guess is not answer:
            print "That was your only chance. The pretty number 7 flies away without you."
            exit(1)
        if guess == answer:
            return 'freedom'

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
    'riddle': Riddle(),
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
