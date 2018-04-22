#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from TicTacToe import TicTacToe
print("\n ***** TIC TAC TOE GAME *****\n")

game = TicTacToe()
print("Do you want to play with computer or with another player?\nIf alone press 1, otherwise press 2.")
while True:
    try:
        number_of_players = int(input())
        if number_of_players != 2 and number_of_players != 1:
            print('Please enter 1 or 2')
            continue
        break
    except ValueError:
        print('Please enter 1 or 2')

if number_of_players == 2:
    game.set_name_player1(input("Player1, what's your name?\n"))
    game.set_name_player2(input("Player2, what's your name?\n"))
    print(game.get_name_player1()+" is playing with sign: " + game.get_symbol_player1())
    print(game.get_name_player2() + " is playing with sign: " + game.get_symbol_player2())
else:
    game.set_name_player1(input("What's your name?\n"))
    print(game.get_name_player1()+", you are playing with sign: " + game.get_symbol_player1())

while True:
    game.print_battlefield()
    try:
        if game.get_next() == 1:
            while True:
                choice = int(input(game.get_name_player1() + " it's your turn. Put your choice (1-9): \n"))
                if game.is_free(choice):
                    game.put_choice(1, choice)
                    break
                print("That position is already taken")
        elif number_of_players == 1 and game.get_next() == 2:
            game.computer_turn()
        else:
            while True:
                choice = int(input(game.get_name_player2() + " it's your turn. Put your choice (1-9): \n"))
                if game.is_free(choice):
                    game.put_choice(2, choice)
                    break
                print("That position is already taken")

        if game.status_of_the_match() != 0:
            break
    except ValueError:
        print('Please enter an integer in range (1-9)')
        continue
game.print_battlefield()

if game.status_of_the_match() == 1:
    print(game.get_name_player1()+" won this match.")
elif game.status_of_the_match() == 2:
    print(game.get_name_player2() + " won this match.")
elif game.status_of_the_match() == 3:
    print("Nobody won this match ¯\_(ツ)_/¯ ")

