import socket, pickle

HOST = 'localhost'
PORT = 50007

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

conn.close()