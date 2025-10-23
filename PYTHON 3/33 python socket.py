# importing socket modulue
import socket
import sys


# AF_INET for ipv4 address-family, SOCK_STREAM for TCP protocol
try:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Successfully")

except socket.error as err: 
    print("Connectioin not created, failed! %s"%(err))


# Default port = 80
port=80

try:
    host_ip= socket.gethostbyname('www.google.com')
    print(host_ip)

except socket.gaierror:
    print("Connection Failed %s")
    sys.exit()


s.connect((host_ip,port))

print("Connected to Google Successfully")




