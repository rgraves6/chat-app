import socket
import select
import sys

HEADER_LENGTH = 20

Port = 12345
IP = "127.0.0.1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, Port))

message = ""
username = input("Welcome to the chat!\nPlease enter your name: ")