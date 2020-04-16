import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2454))
s.listen(5)


while True:
    clientsocket, adderss = s.accept()
    print("Connection from {} has been established".format(adderss))
    clientsocket.send(bytes("Welcom to server", "utf-8"))

