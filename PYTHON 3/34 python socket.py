
# Server side connection

import socket

s = socket.socket()
print("Socket created successfully")

#print(s)

# port of your computer
port = 80


# ip
port = socket.gethostbyname('www.google.com')

# Bind port
s.bind((' ', port))
print("Socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")


# Creating a server side connection
while(True):
    # Establish connection with client.

    c, addr = s.accept()
    print("Got connection from ", addr)

    c.send("Hello world".encode())

    c.close()

    break

    
