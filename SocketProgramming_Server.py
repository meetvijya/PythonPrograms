# Socket programming
import socket

s = socket.socket()
s.bind(('localhost', 9999))
print("Socket created")

s.listen(3)
print('Waiting for Clients...')
while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print("Client connected", address, name)
    c.send(bytes('Welcome to Vijya.com {0}'.format(name), 'utf-8'))
    c.close()









