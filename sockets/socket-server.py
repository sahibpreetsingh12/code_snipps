import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((socket.gethostname(), 1235))
# parameters are First is the IP of localmachine to which we want server to listen to client calls and second is port number 
s.listen(5) # Make Queue of 5 Client-Server Connections

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print("Connection from {} has been established.".format(address))
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()
    
'''
First of all we import socket which is necessary.

Then we made a socket object and reserved a port on our pc.

After that we binded our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well.But we would have passed IP of localhost then it would have listened to only those calls made within the local computer. 

After that we put the server into listen mode.5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.

At last we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets.

'''