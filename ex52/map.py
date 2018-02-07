# -*- coding: utf-8 -*-
class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

#setting scenes

opening_scene = Scene ("Start", "opening_scene",
"""
___$$$___$$$_______________$$$___$$$____
__$$$$$_$$$$$_____________$$$$$_$$$$$___
__$$$$$$$$$$$_____________$$$$$$$$$$$___
____$$$$$$$_________________$$$$$$$_____
______$$$_____________________$$$_______
_______$_______________________$________

Welcome to the game of love, a game in which you can decide how the most beautiful
thing in the world turns out for YOU!

Be my Valentine is a fictional game about love, taking place on the
day of love - Valentine's day.

This year you will have a date with a wonderful human being and only YOU can
decide, how this turns out for you.

Do you feel ready for a trip full of love, emotions and happiness (or loneliness,
emotions and sadness - depends on you)?

'yes'? 'no'?

""")

opening_yes = Scene ("Love is in the Air", "opening_yes",
"""
Good choice. Love is in the air - i feel it! Enjoy your trip in the name of love.

Type 'continue'.
""")

opening_no = Scene("L-O-V-E is the Answer", "opening_no",
"""
Ha. If you weren't interested you have never gotten here in the first place. So
let's skip all this asking and start right away.

Type 'continue'.
""")

help_system = Scene("Need Help?", "help_system",
"""
Before we start this game, I have to provide you with some further information.
This game is a fictional one. You can compare it a little to games like Sims with
the communication between two people. There is no false and no right, there are
only different outcomings.

But I can show you, what you can do at each scene. You can open up the instructions
right now and have a sneak peak on them.  AND you can also open them up at each
scene so that you will know what you can do there when you are right at it.

'yes'? 'no'?
""")

help_instructions = Scene("Help Instructions", "help_instructions",
"""
Need help?

Here are your instructions, sorted by their appearance throughout the game:

________________________________________________________________________________

Looking for: 'f' or 'm'
Restaurant: 'kiss cheek' or 'handshake'
Bar: 'kiss cheek' or 'wave hi'
Kiss Cheek in Bar: 'bill split'
Kiss Cheek in Restaurant: 'compliments' or 'shopping'
Handshake in Restaurant: 'compliments' or 'cars'
Wave: 'continue'
Compliments in Restaurant: 'continue'
Cars: 'continue'
Shopping: 'continue'
Female Question: 'eagles'
Male Question: '17'
Right Answer: 'pay', 'let pay' or 'split'

________________________________________________________________________________

Type 'exit' to leave help mode.
""")

help_no = Scene("Skipped Manual", "help_no",
"""
Okay. Remember, you can come back to the help manual whenever you are stuck. But
as a kind of punishment, you have to start over then for not remembering these
simple answers.

Just type 'help' in every scene starting with the Looking for Scene.

Type 'continue'.
""")

looking_for = Scene("Looking for", "looking_for",
"""
To get the game all set, tell me: What gender are you looking for in a partner?

Type 'f' or 'm'.
""")

restaurant = Scene("Restaurant", "restaurant",
"""
Your Valentine's date takes place in one of the most fanciest restaurants in town.
You enter the room and are totally flashed by the looks of it. A restaurant all
dressed in white with a warm lighting and white peonies on every table.

The seater leads you to a small, round table covered for two with some beautiful
silver cutlery, stunning glasses, bright white candles and napkins folded like two
kissing swans.

This could be a great evening. IF you would not sit there alone and your partner
would already be there.

After some sips on the water glass, your partner suddenly stands right in front
of you and excuses for being a little late.

How do you welcome your date?
""")

in_bar = Scene("Bar", "in_bar",
"""
Your date invites you over to a cute little bar furnished with upholstered sofas,
oldschool lamps and some retro interior pieces such as a cuckoo clock, crotched
desk covers and a lot of plastic flowers.

It seems a bit cheesy when you first enter the room. But as you eyeball through
the room and your eyes meet the one's of your date, that cheesy feeling vanishes
all of a sudden.

How do you welcome your date?
""")

welcome_kisscheek_bar = Scene("Kiss Cheek", "welcome_kisscheek_bar",
"""
You give your date a small kiss on the cheek. Your first real body contact.
Congratulations!

As your partner doesn't turn away and lets you kiss the cheek, it seems that
there is maybe real interest. Let's see how it goes on.

After a few rounds of delicious drinks in a more than comfortable atmosphere, you
get a little tipsy and laugh about literally everything your counterpart is saying.
It is really a great evening and leads to a heavy night out until in the early
morning hours. You seem to be pretty entertaining for each other!

And: Your date took over the first bill in the first bar of the evening and since
then everything is split. That could end up pretty great.

Type 'continue'.
""")

welcome_kisscheek_restaurant = Scene("Kiss Cheek", "welcome_kisscheek_restaurant",
"""
You give your date a small kiss on the cheek. Your first real body contact.
Congratulations!

As your partner doesn't turn away and lets you kiss the cheek, it seems that
there is maybe real interest. Let's see how it goes on.

You spend a really great evening together with a lot of laughing, some small
moments of physical contact, a lot of looking in the eyes. This could really be
a successful date for Valentine's Day. And you happen to feel even a little
butterflies in your stomach. What a date night.

How would you like the conversation to go on?
Do you rather want to give your counterpart some compliments or talk about your
excessive shopping trip earlier that day?
""")

welcome_handshake_restaurant = Scene("Handshake", "welcome_handshake_restaurant",
"""
Uff, a handshake seems to be pretty distant and you can't really get what your
partner really thinks about you. But maybe this changes when getting into deeper
talking.

You order some of the most amazing dishes you have ever heard of, some oysters as
a starter, truffle pasta for main and chocolate lava cake as dessert, and starting to
talk about everything popping into your heads.

How would you like the conversation to go on?
Do you rather want to give your counterpart some compliments or talk about your
deep interest in fast cars?
""")


welcome_wave = Scene("Wave", "welcome_wave",
"""
Ouch, your try to kiss your date on the cheek goes wrong and ends up in a weird
little wave without any kind of body contact and warmth. Your date doesn't seem
to be really interested. Seems like the end of your date comes earlier than expected.

But let's see. Type 'continue'.
""")

convo_compliments_restaurant = Scene("Giving Compliments",  "convo_compliments_restaurant",
"""
You throw several compliments about eyes, hair and the clothes your partner is
wearing. But keep attention: Don't overdo them. Less is more. Spare some for
upcoming dates!

Type 'continue'.
""")

convo_cars = Scene("Cars Forever", "convo_cars",
"""
Audi, Mercedes and Lamborghini are only a few of your favorite car brands.
Throughout the conversation you juggle with terms such as horsepower, motor and
the newest in automobile industry.

Your date is not interested in cars anyhow and all of a sudden leaves without a
warning. Maybe you could have talked a little less about what interests you.

Type 'continue'.
""")

convo_shopping = Scene("I Love Shopping",  "convo_shopping",
"""
Winter sale is happening right now! And all you can think about is whether or not
you should keep all the stuff you bought today. You start showing your partner
a heavy amount of selfies with a new jacket, new shoes, sunglasses etc. and

Remember: You are only getting to know your counterpart tonight and you should not
frighten your date with shopping issues right away. Maybe you could have talked
a little less about what interests you.

Type 'continue'.
""")

quest_f = Scene("Question", "quest_f",
"""
In the conversation you got a question that isn't that easy and proofs a little
if you two are compatible or not.

The question: Which team won the 2018 Superbowl? Choose wisely!
""")

quest_m = Scene("Question", "quest_m",
"""
In the conversation you got a question that isn't that easy and proofs a little
if you two are compatible or not.

The question: What is 35 * 2 - 50 + 8 - 16 + 5?
""")

quest_yes = Scene("Right Answer!", "quest_yes",
"""
Yeah, you got that right! Your date is impressed and likes you even more.

This was actually quite a great night until now! Good job! But there is this one
weird situation at the end of every date. Also here, of course:
Who pays the bill? You, the other, or do you split?
""")

bill_you = Scene("Bill on You", "bill_you",
"""
Before you can wrap your head around it any longer, your partner tells you about
leaving the portemonnaie at home. That's not cool. You have to pay for all.

Type 'continue'.
""")

bill_other = Scene ("Bill on Date", "bill_other",
"""
Because there were a lot of drinks involved tonight, you have to use the toilet.
When you're away, your date pays all of the bill without even hesitating. That's
pretty thoughtful. You like that.

You two go outside your date place. After spending a whole evening together, the
OTHER weird part occurrs - the one where every effort could be crashed immediately.
The goodbye.

Type 'continue'.
""")

bill_split = Scene ("Bill Split", "bill_split",
"""
After ordering the bill, you both grab your cash and pay everything you had.
You split the bill. Cool way of doing it! Save your money for later dates.

You two go outside your date place. After spending a whole evening together, the
OTHER weird part occurrs - the one where every effort could be crashed immediately.
The goodbye.

Type 'continue'.
""")

quest_night = Scene ("Wanna Stay Overnight?", "quest_night",
"""
- Do we want to go to my place? -
This question echoes in your head for a few seconds. What is your date even thinking?
Nothing, seems so. You should end the date.

Type 'continue'.
""")

quest_again = Scene ("Wanna See Me Again?", "quest_again",
"""
Your partner wants to see you again and asks you whether or not you feel the same.

I know, you already felt butterflies flying around on the first date.

So your answer HAS to be 'yes'.
""")

date_end = Scene ("Date End", "date_end",
"""
Wow, that didn't turn out well. You spend Valentine's Day alone. And maybe you'll
stay alone even longer. You can start over.

Type 'start'.
""")

couple_alarm = Scene("Couple Alarm", "couple_alarm",
"""
After several dates and a sweet time together, you start to think about your
better half a lot. And when you open up your mail today, you find a note saying:

Type 'read'.
""")

letter = Scene("Love Letter", "letter",
"""
_$$$$$$___$$$$$$_
$$$$$$$$_$$$$$$$$
$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$_
___$$$$$$$$$$$___
_____$$$$$$$_____
_______$$$_______
________$________
_________________
__$$$$$___$$$$$__
__$$$$$___$$$$$__
__$$$$$___$$$$$__
__$$$$$___$$$$$__
__$$$$$$_$$$$$$__
___$$$$$$$$$$$___
____$$$$$$$$$____

Congratulations! You are loved. Enjoy your trip in the relationship world.

And they all lived happily everafter. Happy Valentine's Day! The end.

If you want to play again, type 'yes'.
""")

the_end = Scene("The End", "the_end",
"""
I said before: If you need help, you could've looked up the help instructions
from the bar/restaurant scene onwards. When I've already given you possible
answers, don't be dumb and follow th instructions!
But if you don't even understand this simple thing, I cannot help you. Sorry. You need
to start over.
""")

#setting answers

opening_scene.add_paths({
    'yes': opening_yes,
    'no': opening_no,
    '*': the_end
})

opening_yes.add_paths({
    'continue': help_system,
     '*': the_end
})

opening_no.add_paths({
    'continue': help_system,
    '*': the_end
})

help_system.add_paths({
    'yes': help_instructions,
    'no': help_no,
    '*': the_end
})

help_instructions.add_paths({
    'exit': looking_for,
    '*': the_end
})

help_no.add_paths({
    'continue': looking_for,
    '*': the_end
})

looking_for.add_paths({
    'f': restaurant,
    'm': in_bar,
    'help': help_instructions,
    '*': the_end
})

restaurant.add_paths({
    'kiss cheek': welcome_kisscheek_restaurant,
    'handshake': welcome_handshake_restaurant,
    'help': help_instructions,
    '*': the_end
})

in_bar.add_paths({
    'kiss cheek': welcome_kisscheek_bar,
    'wave hi': welcome_wave,
    'help': help_instructions,
    '*': the_end
})

welcome_kisscheek_bar.add_paths({
    'continue': bill_split,
    '*': the_end
})

welcome_kisscheek_restaurant.add_paths({
    'compliments': convo_compliments_restaurant,
    'shopping': convo_shopping,
    'help': help_instructions,
    '*': the_end
})

welcome_handshake_restaurant.add_paths({
    'compliments': convo_compliments_restaurant,
    'cars': convo_cars,
    'help': help_instructions,
    '*': the_end
})

welcome_wave.add_paths({
    'continue': date_end,
    'help': help_instructions,
    '*': the_end
})

convo_compliments_restaurant.add_paths({
    'continue': quest_m,
    'help': help_instructions,
    '*': the_end
})

convo_cars.add_paths({
    'continue': date_end,
    'help': help_instructions,
    '*': the_end
})

convo_shopping.add_paths({
    'continue': date_end,
    'help': help_instructions,
    '*': the_end
})

quest_f.add_paths({
    'eagles': quest_yes,
    'help': help_instructions,
    '*': the_end
})

quest_m.add_paths({
    '17': quest_yes,
    'help': help_instructions,
    '*': the_end
})

quest_yes.add_paths({
    'pay': bill_you,
    'let pay': bill_other,
    'split': bill_split,
    'help': help_instructions,
    '*': the_end
})

bill_you.add_paths({
    'continue': quest_night,
    'help': help_instructions,
    '*': the_end
})

bill_other.add_paths({
    'continue': quest_again,
    'help': help_instructions,
    '*': the_end
})

bill_split.add_paths({
    'continue': quest_again,
    'help': help_instructions,
    '*': the_end
})

quest_night.add_paths({
    'continue': date_end,
    'help': help_instructions,
    '*': the_end
})

quest_again.add_paths({
    'yes': couple_alarm,
    'help': help_instructions,
    '*': the_end
})

date_end.add_paths({
    'start': opening_scene,
    'help': help_instructions,
    '*': the_end
})

couple_alarm.add_paths({
    'read': letter,
    'help': help_instructions,
    '*': the_end
})

letter.add_paths({
    'start': opening_scene,
    'help': help_instructions,
    '*': the_end
})

the_end.add_paths({
    'start': opening_scene,
    'help': help_instructions,
    '*': the_end
})

#setting urls

SCENES = {
	opening_scene.urlname : opening_scene,
	opening_yes.urlname : opening_yes,
	opening_no.urlname : opening_no,
	help_system.urlname : help_system,
	help_instructions.urlname : help_instructions,
	help_no.urlname : help_no,
	looking_for.urlname : looking_for,
	restaurant.urlname : restaurant,
	in_bar.urlname : in_bar,
	welcome_kisscheek_restaurant.urlname : welcome_kisscheek_restaurant,
	welcome_kisscheek_bar.urlname: welcome_kisscheek_bar,
	welcome_handshake_restaurant.urlname : welcome_handshake_restaurant,
	welcome_wave.urlname: welcome_wave,
	convo_compliments_restaurant.urlname : convo_compliments_restaurant,
	convo_cars.urlname : convo_cars,
	convo_shopping.urlname : convo_shopping,
	quest_f.urlname : quest_f,
	quest_m.urlname : quest_m,
	quest_yes.urlname : quest_yes,
	bill_you.urlname : bill_you,
	bill_other.urlname : bill_other,
	bill_split.urlname : bill_split,
	quest_night.urlname : quest_night,
	quest_again.urlname : quest_again,
	date_end.urlname : date_end,
	couple_alarm.urlname : couple_alarm,
    letter.urlname : letter,
	the_end.urlname : the_end
}

START = opening_scene
BACKGROUND = "love.jpg"
