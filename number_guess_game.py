# goal: create simpe game where the player has to guess game and gather points
# rules: player chooses scope 1-10, 1-30, 1-50
# has to collect 100 points
# has 5 attempts. correct answer +5, +10, +20 points ( 1-10, 1-30, 1-50). wring minus same
# won't go below 0
# will have hints. Odd/even always, scope  (e.g 30<y<40 is chosen only for 1-30 and 1-50) points are decreased from 10 to 5, and from 20 to 10 (this warning will be included with the hint if it will be chosen)
# rules
import random


def rules():
    print(f'''Welcome {player_name} to the Number Guessing Game!
            Here is you guide:
          1) First you must difficulty level (easy: 1-10, medium: 1-30 or hard: 1-50).
          2) Your goal is to collect 100 scores.
          3) You have 5 tries to guess the number
          4) If you fail you lose points, if you win, you gain
          Point system:
           - + or - 5 points if the scope is 1-10
           - + or - 10 points if the scope is 1-30
           - + or - 20 points if the scope is 1-50
    ''')
# player name


def get_username():
    while True:
        player = input(
            'Hello, player! please enter your name! (Only letters/digits and no space)')
        cln_player = player.strip()
        if cln_player.isalnum():
            return cln_player
        else:
            print('Oops, please use only letters and digits wiith no space.')

# game dificulty


def game_difficulty():
    print('Please choose the difficulty level of the game ')
    while True:
        try:
            limit = int(input('easy: 10, medium: 30 or hard: 50. '))
            if limit in [10, 30, 50]:
                return limit
            else:
                print('Reminder: limit must be either 10, 30, or 50: ')
        except ValueError:
            print('Please enter the number!')
player_name = get_username()

# generate random intts based on the chosen dificulty level
# give player 5 tries and hiants odd/even
# create function for medium hard level and if player need thhey willcall it

# def generate_number():
#     generated_number = random.randint(1, game_difficulty())
#     if generated_number % 2 == 0:
#         print('The number is even')
#     else:
#         print('The number is odd')
#     return generated_number
# functions so far
# rules() - introduction
# get_username() - defines user
# game_difficulty() - dificulty (This will determine some of the game rules)
# generate_number() - generates number based on the  dificulty
# number_to_guess = generate_number()
difficulty = game_difficulty()
def score_systemm():
    if game_difficulty() == 10:
        score = 5
    elif game_difficulty() == 30:
        score = 10
    else:
        score = 20
    return score
def play_game():
    total_score = 0
    while total_score < 100:
        # number generation
        generated_number = random.randint(1, difficulty)
        if generated_number % 2 == 0:
            print('The number is even')
        else:
            print('The number is odd')
        number_to_guess = generated_number
        tries = 5
        while tries > 0:
            number = int(input('Take a guess! '))
            if number == number_to_guess:
                print('Congratulation! you guessed the number')
                if difficulty == 10:
                    total_score += 5
                elif difficulty == 30:
                    total_score += 10
                else:
                    total_score += 20
                break
            else:
                tries -= 1
                if tries == 0 and total_score > 0:
                    total_score -= score_systemm()
                elif tries ==0 and total_score ==0:
                    total_score == 0
            print(f'Your total score is {total_score}')
    



        

