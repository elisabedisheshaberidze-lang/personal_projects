# # goal: create simpe game where the player has to guess game and gather points
# # rules: player chooses scope 1-10, 1-30, 1-50
# # has to collect 100 points
# # has 5 attempts. correct answer +5, +10, +20 points ( 1-10, 1-30, 1-50). wring minus same
# # won't go below 0
# # will have hints. Odd/even always, scope  (e.g 30<y<40 is chosen only for 1-30 and 1-50) points are decreased from 10 to 5, and from 20 to 10 (this warning will be included with the hint if it will be chosen)
# # rules
# import random
# import turtle
# # player name
# def get_username():
#     while True:
#         player = input(
#             'Hello, player! please enter your name! (Only letters/digits and no space)')
#         cln_player = player.strip()
#         if cln_player.isalnum():
#             return cln_player
#         else:
#             print('Oops, please use only letters and digits wiith no space.')
# player_name = get_username()
# def rules():
#     print(f'''Welcome {player_name} to the Number Guessing Game!
#             Here is you guide:
#           1) First you must difficulty level (easy: 1-10, medium: 1-30 or hard: 1-50).
#           2) Your goal is to collect 100 scores.
#           3) You have 5 tries to guess the number
#           4) If you fail you lose points, if you win, you gain
#           Point system:
#            - + or - 5 points if the scope is 1-10
#            - + or - 10 points if the scope is 1-30
#            - + or - 20 points if the scope is 1-50
#     ''')
# # called function rules. it uses get_username()
# rules()
# print(player_name)
# # game dificulty
# def game_difficulty():
#     print('Please choose the difficulty level of the game ')
#     while True:
#         try:
#             difficulty = int(input('easy: 10, medium: 30 or hard: 50. '))
#             if difficulty in [10, 30, 50]:
#                 return difficulty
#             else:
#                 print('Reminder: limit must be either 10, 30, or 50: ')
#         except ValueError:
#             print('Please enter the number!')
# difficulty_level = game_difficulty()
# # game logic:
# # i need to generate numbers based on the difficulty. odd/even hints will be for all level
# # then i need to create core part. user has 5 tries. if correct, plus points, else - points.
# # i need to make sure during 5 tries the generated number is the same and after that program generates new one
# # to now go below 0 and when it hits 100 reward (that will be funny part)
# # i need to find out how to create hint system for medium/hard level
# def score_system():
#     if difficulty_level == 10:
#         score = 5
#     elif difficulty_level == 30:
#         score = 10
#     else:
#         score = 20
#     return score
# def winner():
#     try:
#         print(f'Congratulation {player_name}! You won the game!')
#         print('Here is a little surprize for you :)')
#         shape = input('Please choose one of this: turtle, circle, square, triangle')
#         cleaned_shape = shape.strip().lower()
#         color = input('Please choose one of this: red, blue, green, orange, black')
#         cleaned_color = color.strip().lower()
#         if not cleaned_shape in [ 'turtle', 'circle', 'square', 'triangle']:
#             raise ValueError('Please choose one of this: turtle, circle, square, triangle')
#         elif not cleaned_shape in ['red', 'blue', 'green', 'orange', 'black']:
#             raise ValueError('Please choose one of this: red, blue, green, orange, black')
#     except ValueError as e:
#         print(e)
#     else:
#         t.turtle.Turtle()
#         t.color(cleaned_color)
#         t.shape(cleaned_shape)
#         t.left(45)
#         t.forward(250)
#
# def play_game():
#     total_score = 0
#     tries = 5
#     while total_score < 100:
#         number_to_guess = random.randint(1, difficulty_level)
#         while tries > 0:
#             try:
#                 if number_to_guess % 2 == 0:
#                     print('The number is even')
#                 else:
#                     print('The number is odd')
#                 guessed_number = int(input('Take a guess! '))
#                 if guessed_number == number_to_guess:
#                     print('Good job! You guessed the number! Here is you point')
#                     total_score += score_system()
#                     print(f'Your total score is {total_score}')
#                     break
#                 else:
#                     print('Oops, not your lucky try! Guess again!')
#                     tries -= 1
#                 if tries == 0:
#                     total_score -= score_system()
#                     print(f'The number was {number_to_guess}! Here is your current score: {total_score}')
#             except ValueError:
#                 print('Hmm... ypu have to guess number. Please enter a number!')
#             if total_score == 100:
#                 winner()
#
#
#
# play_game()
import turtle
import time
def winners_surprise():
    print('Congratulations! You win!')
    time.sleep(2)
    print('I have a surprise :)')
    time.sleep(2)
    print('Ready...')
    time.sleep(2)

    t = turtle.Turtle()
    s = turtle.Screen()
    s.title('Click to exit!')
    s.bgcolor('#f8edeb')
# ok i need to add surprise
winners_surprise()