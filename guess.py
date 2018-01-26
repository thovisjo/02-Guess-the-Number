#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

def random_encounter_generator(num60to89, provision):
        """Randomly chooses between 5 pregenerated scenarios.

        num -> function"""

        if(num60to89 < 66):
                return random_encounter_horde()

        elif(num60to89 < 72):
                return random_encounter_bandits(provision)

        elif(num60to89 < 78):
                return random_encounter_dogs()

        elif(num60to89 < 84):
                return random_encounter_helpinghand(provision)

        elif(num60to89 < 90):
                return random_encounter_deer(provision)

def random_encounter_horde():
        while True:
                dec = str.upper(input("A sea of the living dead stands before you. You must try to sneak past it or return to the door. Please enter \"Return\" or \"Sneak\".\n"))
                if(dec == "SNEAK"):
                        if random.randint(0,100) > 75:
                                print("You have found a can of pineapple juice in a shack. Not much, but it will sustain you for a day.")
                                return 1
                        else:
                                print("The effort was fruitless; there was simply no way around the horde. You return home empty-handed.")
                                return 0
                elif(dec == "RETURN"):
                        print("You turn back in the face of the horde, with nothing to show for your wasted time.")
                        return 0
                else:
                        print("Please enter \"Return\" or \"Sneak\".")

def random_encounter_bandits(amtfood):
        while True:
                dec = str.upper(input("""An armed man, covered in dirt, sits on a blue chair in front of you.""" +
                                      """There is a can of tomato soup under his chair. Will you fight him for the can or leave?\nPlease enter \"Fight\" or \"Leave\".\n"""))
                if(dec == "FIGHT"):
                        if random.randint(0,100) > 50:
                                print("You successfully surprise the gruff man, choking him and stealing his meal. He would do the same, after all.")
                                return 1
                        else:
                                print("The strong man overpowers you and begins to fire at you. You barely escape and, in your haste, drop a can of food.")
                                if amtfood > 0:
                                        return -1
                                else:
                                        return 0
                elif(dec == "LEAVE"):
                        print("You do not trust that you could overpower this man. You return home empty-handed.")
                        return 0

                else:
                        print("Please enter \"Fight\" or \"Leave\".")

def random_encounter_dogs():
        while True:
                dec = str.upper(input("""A group of wild dogs - perhaps once domesticated - are whining outside a door inside an overgrown house.""" +
                                      """\nWill you attempt to open the door? Please enter \"Yes\" or \"No\".\n"""))
                if(dec == "YES"):
                        if random.randint(0, 100) > 50:
                                print("The wild dogs allow you to open the door for them. They begin feasting on the corpse within, distracted while you grab a can of dog food for yourself.")
                                return 1
                        else:
                                print("The wild dogs bark and chase you away from the door. You remain uninjured, but are forced to return to the bunker empty-handed.")
                                return 0
                elif(dec == "NO"):
                        print("Deciding not risk upsetting the canines, you return home without anything to show for your trip.")
                        return 0

                else:
                              print("Please enter \"Yes\" or \"No\".")

def random_encounter_helpinghand(amtfood):
        while True:
                dec = str.upper(input("A man stands alone in a clearing. He is well-armed. Do you approach? Please enter \"Yes\" or \"No\".\n"))
                if dec == "YES":
                        if random.randint(0,100) > 30:
                                print("The man spots you, and waves at you. He has a smile on his face. After a short conversation, he agrees to give you a can of tuna and sends you on your way.")
                                return 1
                        else:
                                print("The man spots you and waves you over. When you get close, however, he holds you at gunpoint and demands a can of food. You are forced to give him one.")
                                if amtfood > 0:
                                        return -1
                                else:
                                        return 0
                elif dec == "NO":
                        print("No other oppurtunities present themselves. You find no food and are forced to return to the bunker with nothing.")
                        return 0

                else:
                        print("Please enter \"Yes\" or \"No\".")

def random_encounter_deer(amtfood):
        while True:
                dec = str.upper(input("A great stag has impaled itself upon a piece of rebar and has died. Will you harvest what you can? Please enter \"Yes\" or \"No\".\n"))
                if dec == "YES":
                        if random.randint(0,100) > 10:
                                print("The stag's meat provides two days of much-appreciated fresh meat to your diet after you collect what you can.")
                                return 2
                        else:
                                print("When you eat the meat, you come to realize it has made you even more starving than before. You are forced to eat a can of food to survive.")
                                if amtfood > 0:
                                        return -1
                                else:
                                        return 0

                elif dec == "NO":
                        print("You cannot risk getting sick from meat, no matter how fresh. You unfortunately return home empty handed.")
                        return 0

                else:
                        print("Please enter \"Yes\" or \"No\".")



#declaring variables

#Guesses which can be depleted by other activities, such as searching for food or being exhausted by lack of food.
hours = 10
#A player can guess between 1 and 100.
guess_range = 100
# The player has 3 nights of food to start with. When it reaches zero, the player will begin to oversleep.
provisions = 3
#Nights are the score.
nights = 0
# Keeps track of whether the player got inside.
inside = 0
# Luck determines whether a scavenging session is successful.
luck = 0
# To exit the game early
end = False

#generate a random integer between 1 and 100 (inclusive) and store it in the variable [number]

# Main set of code

while(hours > 0 and not end):
        nightsSTR = str(nights)
        provisionsSTR = str(provisions)
        print("You have survived " + nightsSTR + " nights. \nYou have " + provisionsSTR + " nights of food.\nEnter \"Quit\" to quit.")
        inside = 0
        combo = random.randint(1,guess_range)
        while(hours > 0 and not end):
                scavOrGuess = input("Would you like to scavenge for food or guess the combo? Each takes one hour.\n")

                if(str.upper(scavOrGuess) == ("SCAVENGE") or str.upper(scavOrGuess) == ("SCAVENGE FOR FOOD") or str.upper(scavOrGuess) == "FOOD"):
                        hours -= 1
                        luck = random.randint(1,100)
                        if(luck < 60):
                                print("You found no food in the overgrown buildings surrounding the bunker.")
                        elif(luck >= 60 and luck <90):
                                provisions = provisions + random_encounter_generator(luck, provisions)
                        elif(luck >= 90):
                                print("You found a delicious, beautiful can of baked beans in the burnt-out rubble of a house. Provisions +1. ")
                                provisions += 1

                elif(str.upper(scavOrGuess) == ("GUESS") or str.upper(scavOrGuess) == ("GUESS THE COMBO") or str.upper(scavOrGuess) == ("COMBO")):
                        while(hours > 0 and not end):
                                #ask the user for a response and store it in the variable [guess]
                                guess = input("Input a combination between 1 and 100.\n")


                                #a try/except block is a great tool for programmers to be able to deal with errors. In this instance, it reports an error if the user enters something other than an integer
                                try:
                                        #convert the guess to an integer
                                        guess = int(guess)

                                #check if the guess is less than the random number
                                        if guess < combo:
                                                print('Too low!')
                                                hours -= 1

                                        elif guess > combo:
                                                print("Too high!")
                                                hours -= 1

                                        elif guess == combo:
                                                print("You got in!")
                                                nights += 1
                                                hours = 10
                                                inside = 1
                                                break

                                        hoursSTR = str(hours)
                                        print("You have " + hoursSTR + " hours left.")
                                except ValueError:
                                        if str.upper(guess) == "QUIT":
                                                end = True
                                        else:
                                                print('Please enter a whole number.')
                        if(inside == 1):
                                break
                elif(str.upper(scavOrGuess) == "QUIT"):
                     end = True
        if(provisions == 0):
                hours -= random.randint(2, 6)
                hoursSTR = str(hours)
                print("Due  to lack of food, you overslept. You only have " + hoursSTR + " hours today.")
        elif(provisions > 0):
                provisions -= 1

print("You have died. You survived " + nightsSTR + " nights.")
