import socket, pickle
from TicTacToe import TicTacToe
from GuessNumber import GuessNumber

HOST = 'localhost'
PORT = 50007
SERVER_STATUS = 0

while SERVER_STATUS == 0:
    print("SERVER IS ONLINE")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    conn.send(pickle.dumps(1))

    while 1:
        data = conn.recv(4096)
        if data:
            #conn.send(data)
            data_arr = pickle.loads(data)
            print("RECEIVED: ", repr(data_arr))
            if data_arr[0] == 1:
                #GAME INITIALIZATION:
                if data_arr[3] == 1:
                    print("STARTING TIC TAC TOE")
                    game = TicTacToe()
                    if data_arr[1] == 1:
                        SERVER_STATUS = 1
                    else:
                        SERVER_STATUS = 2
                    break
                elif data_arr[3] == 2:
                    print("STARTING GUESS NUMBER")
                    game = GuessNumber()
                    if data_arr[1] == 1:
                        SERVER_STATUS = 1
                    else:
                        SERVER_STATUS = 2
                    break
    while SERVER_STATUS == 2:
        raise NotImplementedError #NOT IMPLEMENTED YET
    while SERVER_STATUS == 1:
        while 1:
            data = conn.recv(4096)
            if data:
                # conn.send(data)
                data_arr = pickle.loads(data)
                print("RECEIVED: ", repr(data_arr))

    conn.close()