#
# CHRISTIAN RIVA
# EWA GIERLACH
#
#
from TicTacToeClientConnection import TicTacToeClientConnection

HOST = 'localhost'
PORT = 10009

connection = TicTacToeClientConnection(HOST,PORT)
playername = input("insert your name: ")
number_of_player = input("Singleplayer [1] or Multiplayer [2]: ")

if connection.connect()==1:
    print("Connected")
    connection.initial_settings(number_of_player,playername)

#connection.close_connection()