# goal: create simpe game where the player has to guess game and gather points
# rules: player chooses scope 1-10, 1-30, 1-50
# has to collect 100 points
# has 5 attempts. correct answer +5, +10, +20 points ( 1-10, 1-30, 1-50). wring minus same
# won't go below 0
# will have hints. Odd/even always, scope  (e.g 30<y<40 is chosen only for 1-30 and 1-50) points are decreased from 10 to 5, and from 20 to 10 (this warning will be included with the hint if it will be chosen)
# define player
# name must be letters, digits and underscore is allowed
import random


def rules():
    print('''Welcome to the nNumber Guessing Game!
            Here is you guide:
          1) First you must choose scope (1-10, 1-30 or 1-50).
          2) Your goal is to collect 100 scores.
          3) You have 5 tries to guess the number
          4) If you fail you lose points, if you win, you gain
          Point system:
           - + or - 5 points if the scope is 1-10
           - + or - 10 points if the scope is 1-30
           - + or - 20 points if the scope is 1-50
    ''')


def get_username():
    while True:
        player = input(
            'Hello, player! please enter your name! (Only letters/digits/underscore and no space)')
        cln_player = player.strip()
        for char in cln_player:
            if not char.isalnum or not char == '_':
                print('Oops, please enter correct username!')
            else:
                return cln_player


print(get_username())
