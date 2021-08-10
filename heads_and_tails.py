import random

def start_game():
    '''Every time flip the coin, add the ordinal number to the winning side.
    The EXAMPLE: 1'st round winner gets 1 point, 15th round winner gets 15 points. etc.
    '''
    flip,heads,tails = 0,0,0

    while flip < 20: #You can set the number of turns here
        coin = random.randint(1,2)
        if coin == 1:
            flip += 1
            heads += flip
        else:
            flip += 1
            tails += flip

    if heads == tails:
        print('Game is equal!')
    elif heads > tails:
        print('Heads WIN')
    else:
        print('Tails WIN')
    print('Tails score is:', tails,'\n' 'Heads score is:',heads)

start_game()
