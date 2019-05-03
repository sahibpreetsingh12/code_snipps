'''

Socket programming is a way of connecting two nodes on a network to communicate with each other. 
One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. 
Server forms the listener socket while client reaches out to the server.

'''


# The Python function socket.gethostname() returns the host name of the current system under which the Python interpreter is executed.


import socket

# Get the local host name

HostName = socket.gethostname()

print("Name of the localhost is {}".format(HostName))

 

# to Get the IP address of the local host

HostIP = socket.gethostbyname(HostName)

print("IP address of the localhost is {}".format(myIP))
