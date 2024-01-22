from random import choice

opciones = ["piedra", "papel", "tijera"]
option_win = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

def go_game():
    amount_player = input("Input 1 for only player or 2 for two player: ")
    if amount_player == "1":
        print('Playing against the computer')
        validate_tie(1)
    
    elif amount_player == "2":
        print('Playing with other player')
        validate_tie(2)
    
def validate_tie(player):
    option_user, option_x = None, None
    while True:    
        option_user = input('Input one player option piedra/papel/tijera: ')
        if player == 1:
            option_x = choice(opciones)
        elif player == 2:
            option_x = input('Input two player option piedra/papel/tijera: ')
        
        if option_user != option_x:
            break

    validate_win(option_user, option_x, player)



def validate_win(option_user, option_x, player):
    if option_win[option_user] == option_x: 
        if player == 1: print('You win')
        elif player == 2: print('Win the player 1')
    else:
        if player == 1: print('You lose')
        elif player == 2: print('Win the player 2')

go_game()