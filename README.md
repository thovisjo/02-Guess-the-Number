# 02-Guess-the-number

In this guess the number game, I wanted to play around with certain aspects of the game.
In most guess the  number games, the game is over once the number is guessed.
This one plays more like an older game focused on high scores; the game ends
after the player fails to guess the number.

Though the game systems are functional, I believe it could use work.

The basics of the game:
* There are 10 hours to attempt to open the door, which is locked with a code.
* The code is cracked via the guess the number game, from 1-100.
* Since it takes, at maximum, seven tries to correctly guess a number from 1-100, there would be no way to lose, unless
* There's a system in place to prevent winning forever. The player will slowly lose food,
* and, once the player starts being hungry, at zero food, they will oversleep.
* This will lower the amount of hours the player has to guess the code.
* To try to survive longer, the player can search for food, spending valuable hours.
* The chances of gathering food  are random, and include 5 random encounters which have choices.
* Even with this system in place, the player will still slowly lose food.
* The player can also quit at any time other than in a random encounter by typing quit.

Things that could be further improved:
* On the random encounters and other response driven questions, the input is functional but finnicky.
* More random encounters.
* More description to increase interest in the game.
* Fix the provisions counter so that it is more accurate (Kinda fixed)
* Describe the systems within the game more clearly.
* Allow significantly more input options.
* Better balance the scavenge system; its a little too rewarding.
* Clean up the code just a little.

Code wise, there are many features within the game:
* While and nested while loops. I chose a while loop so that the game could be exited manually and to better determine when the game ends.
* There are functions within the code for each of the random encounters. This allows them to be possibly used later.
* Everything that has a chance of failing is randomly determined, similar to a dice roll in D&D
* if, elif, and else all find there way into the code at various points.
* While loops are also used in the functions of the random encounters to prevent typos affected choices.
* Practically every string printed has escape characters.

That's about it!
