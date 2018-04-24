#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from TicTacToeClientConnection import TicTacToeClientConnection
from tabulate import tabulate

HOST = 'localhost'
PORT = 10009

connection = TicTacToeClientConnection(HOST,PORT)
playername = input("insert your name: ")
number_of_player = int(input("Singleplayer [1] or Multiplayer [2]: "))
which_game = int(input("TicTacToe [1] or GuessNumber [2]: "))

if connection.connect()==1:
    print("Connected")
    connection.initial_settings(number_of_player,playername,which_game)

#connection.close_connection()