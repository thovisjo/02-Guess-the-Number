#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

#variables
guesses = 10
guess_range = 20


#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
number = random.randint(1,guess_range)

#ask the user for a response and store it in the variable [guess]
guess = input()


#a try/except block is a great tool for programmers to be able to deal with errors. In this instance, it reports an error if the user enters something other than an integer
try:
	#convert the guess to an integer
	guess = int(guess)

	#check if the guess is less than the random number
	if guess < number:
		print('Too low!')

except ValueError:
	print('Please enter a whole number.')
