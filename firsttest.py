import socket

while True:
    ip = input("Enter Name: ")
    if ip == "exit":
        print("Thank You")
        break
    else:
        print(socket.getservbyname(ip))
