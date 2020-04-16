import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 2454))

mes = s.recv(1024)
print(mes.decode("utf-8"))