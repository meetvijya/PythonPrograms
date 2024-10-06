# Socket Programming

import socket
c = socket.socket()

c.connect(('localhost', 9999))
name = input('Enter Client Name')
c.send(bytes(name, 'utf-8'))
print("Server: " + c.recv(1024).decode())

