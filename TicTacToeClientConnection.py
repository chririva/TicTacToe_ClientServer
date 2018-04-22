import socket, pickle

class TicTacToeClientConnection:
    HOST = 'localhost'
    PORT = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, HOST, PORT):
        self.HOST=HOST
        self.PORT=PORT

    def connect(self):
        self.s.connect(('localhost', 50007))
        while 1:
            data = self.s.recv(4096)
            if data:
                data_received = pickle.loads(data)
                if data_received==1:
                    return 1
                return 0
    def close_connection(self):
        self.s.close()
    def initial_settings(self,number_of_player,my_name):
        data_to_send = ([1,number_of_player,my_name])
        arr = pickle.dumps(data_to_send)
        self.s.send(arr)
        data = self.s.recv(4096)
        data_received = pickle.loads(data)
