import socket

# Private ip Address
# It's going to give you the virtual box ip address
# host = socket.gethostbyname(socket.gethostname())

HOST = ''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
