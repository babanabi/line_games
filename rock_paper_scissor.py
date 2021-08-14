import random
import time

def user_choice():
    '''define user choice'''
    x = True
    while x:

        choice = input('Please enter rock, paper or scissor: ')
        choice = choice.lower()
        if choice in ['rock','paper','scissor']:
            return choice
            x == False
            break

        else:
            print ( 'Invalid input. Pleaase re-enter (rock,paper,scissor): ')
            x == True


def comp_choi():
    '''define computer choice'''
    my_list = ['rock','scissor','paper']
    return random.choice(my_list)


def on_game(player1,player2):
    '''determine winner'''

    if player1 == 'paper' and player2 == '1':
        return 'Well done!'

    elif player1 == 'paper' and player2 == 'scissor':
        return 'Upsss'

    elif player1 == 'rock' and player2 == 'scissor':
        return 'Well done!'

    elif player1 == 'rock' and player2 == 'paper':
        return 'Upsss'

    elif player1 == 'scissor' and player2 == 'paper':
        return 'Well done!'

    elif player1 == 'scissor' and player2 == '1':
        return 'Upsss'
    else:
        player1 == player2
        return 'brrrrr'


# Loop game trough While till player dicide end up game.
# using for loop playing 3 times and determine winner by if statement and boolians.
game_on = True


while game_on:


    user_score = 0
    comp_score = 0
    for x in range(3):
        result = on_game(user_choice(),comp_choi())
        time.sleep(2)
        if result == 'Well done!':
            user_score = user_score + 1
            print('Well Done!')
            print(user_score,' : ',comp_score)
        elif result == 'Upsss':
            comp_score = comp_score + 1
            print('Upsss')
            print(user_score,' : ',comp_score)
        else:
            result == 'brrrrr'
            user_score = user_score + 1
            comp_score = comp_score + 1
            print('brrrrr')
            print(user_score,' : ',comp_score)

    if user_score > comp_score:
        print ('You WIN !')
    elif user_score < comp_score:
        print ('Computer WIN !')
    else:
        user_score == comp_score
        print ('Game Tie')


    on = True
    while on:
        try:
            decision = input('Do yo want play again: y or n')
            decision = decision.lower()
            if decision not in ['y','n']:
                print ('Invalid input! Choose (y or n): ')
                on = True
            elif decision == 'n':
                print('Game Over')
                game_on = False
                on = False

            else:
                decision == 'y'
                print('Game on')
                game_on = True
                on = False

        except:
            print('Something is went wrong try again!')
