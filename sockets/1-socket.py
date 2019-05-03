'''
The Python function socket.gethostname() returns the host name of the current system under which the Python interpreter is executed.
'''

import socket

# Get the local host name

HostName = socket.gethostname()

print("Name of the localhost is {}".format(HostName))

 

# to Get the IP address of the local host

HostIP = socket.gethostbyname(HostName)

print("IP address of the localhost is {}".format(myIP))