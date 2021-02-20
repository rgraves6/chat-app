import socket
import select
import sys
from _thread import *
HEADER_LENGTH = 20
IP = "127.0.0.1"
Port =12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, Port))
server_socket.listen(100)
clients = []
msg=""
def Threading(a, b):
    a.send("Establishing connection...".encode())
    while True:
            try:
                message = a.recv(HEADER_LENGTH)
                if message:
                    print (message.decode())
                    show(message, a, 0)
                else:
                    if a in clients:
                        clients.remove(a)
            except:
                continue
def show(message, a, number):
    if number!=a:
        try:
            number.send(message.encode())
        except:
            if number in clients:
                clients.remove(number)
    return show(message, a, number+1)
    while True:
        a, b = server_socket.accept()
        clients.append(a)

        print ("New User connected!")

        start_new_thread(Threading,(a, b))
