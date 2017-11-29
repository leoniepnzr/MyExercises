from sys import exit

def start():
    print "Welcome to another incredible maze game. Type \"start\" if you dare and \"exit\" to leave!"
    print "Please note: Always answer in lowercase letters."

    while True:
        choice = raw_input("> ")

        if choice == "start":
            print "Yay! But are you really sure? Type \"yes\" or \"no\" to get started."
            while True:
                choice = raw_input("> ")

                if choice == "yes":
                    print "Ok, let's get started:"
                    room()
                else:
                    game_over("Knew it, you scaredy cat!")
        elif choice == "exit":
            print "Boo!"
            exit(0)
        else:
            game_over("Learn to make decisions, dumbass!")

def room():
    print "\nAfter a rough night, you find yourself waking up with nothing but a \nhuge bagpack and a swimsuit alone in a room with absolutely no idea what happened last night."
    print "You are surrounded by 6 lifeless bodies."
    print "There is a knife on your left, on your right you find a gun."
    print "Which one do you take?"

    while True:
        choice = raw_input("> ")

        if choice == "knife":
            knife()
        elif choice == "gun":
            gun()
        else:
            print "I will ask you one more time: knife or gun?"
            print "This is a live-or-die-decision, take it serious!"

            choice = raw_input("> ")

            if choice == "knife":
                knife()
            elif choice == "gun":
                gun()
            else:
                print "You think you're funny right? Follow the damn instructions, you idiot, or \nleave this game, goddamnit."
                exit(0)

def knife():
    print "You put the knife in the bagpack. Then you enter the only door you see \nthat leads you to another room."
    print "In the middle of this room, there is a table with two things on it: A \nwhite pill and a bottle with see-through liquid."
    print "Which item do you put in your bagpack? \"pill\" or \"bottle\"? Choose one."

    while True:
        choice = raw_input("> ")

        if choice == "pill":
            pill()
        elif choice == "bottle":
            bottle()
        else:
            print "There are no other options."

def gun():
    print "Fully weaponed with a loaded gun you dare to approach the only door \nyou see in the room, that may lead you outside."
    print "That's when you hear some strange noises from behind the door."
    print "Do you enter the door anyways?"

    while True:
        choice = raw_input("> ")

        if choice == "no":
            game_over("Go to bed and get rid of your hangover! You're boring.")
            exit(0)
        elif choice == "yes":
            print "The party people already missed you!"
            print "You re-enter the crazy weekend \npool party with your loaded water gun. Have fun and keep partying!"
            exit(0)
        else:
            print "It takes years for you to make a decision. Grow up!"
            exit(0)

def pill():
    print "On your way to find an exit of this freaking maze, you get to meet a \ncreepy creature with women's clothes and an ugly face."
    print "The creature threatens you and wants you to give the pill to her unless \nyou want to pass the door behind her."
    print "What do you do?"
    print "\"give\" it the pill, beguile it with \"fake compliments\" or \"keep\" the pill for yourself?"
    creature_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "give":
            game_over("You die of bad headache, the pill was Aspirin and might have cured \nyour hangover. Rough night, huh?")
        elif choice == "keep" and not creature_moved:
            game_over("You realize that the creature is your girl. Your hungover girlfriend \nbreaks up with you because of your selfishness.")
        elif choice == "fake compliments" and not creature_moved:
            print "The creature aka your wasted girlfriend with wasted make up all over her \nface feels flattered and let's you leave through the door. You only have to \"open door\". Just. Leave. Now."
            creature_moved = True
        elif choice == "fake compliments" and creature_moved:
            game_over("I told you to leave! Your awfully wasted looking girlfriend now gets you are faking compliments \nand slaps you. That turned out wrong!")
        elif choice == "open door" and creature_moved:
            print "Enjoy your hangover breakfast with the butter knife and the Aspirin in your bagpack!"
            free()
        else:
            print "I only want to help you to go through this. Choose wisely."

def bottle():
    print "You are so thirsty and you decide to empty the bottle all at once."
    game_over("You die of alcohol poisoning. It was leftover vodka from last night in the bottle.")

def free():
    print "You are free now. Get better soon! You really have a fertile hangover imagination, son."
    print "Leave the alcohol be next time."
    exit(0)

def game_over(why):
    print why, "Game over!"
    exit(0)

start()
