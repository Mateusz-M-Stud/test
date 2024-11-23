###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer_roll = random.randint(1, 6)  # The computer rolls the dice
# YOUR TURN
user_guess = int(input('Guess the number on the dice (1 to 6): '))

if user_guess == computer_roll:
    print(f'You won: True')
else:
    print(f'You won: False')