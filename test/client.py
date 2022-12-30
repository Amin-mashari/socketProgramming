# Import socket module
import socket
from decouple import config

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
DOMAIN = config('domain')
PORT = config('port')

# connect to the server on local computer
s.connect((DOMAIN, PORT))

# receive data from the server
print(s.recv(1024))
# close the connection
s.close()
