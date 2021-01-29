import socket
host = socket.gethostname()
#In case you want to access a specific computer while many of them are availlable
port = int(input("Enter Your Port Number"))
try:
    s = socket.socket()
    s.connect((host, port))
    s.sendall(b'Welcome User!')
    data = s.recv(1024)
    s.close()
    print(repr(data)) 
except ConnectionRefusedError:
    print("You took to long to join a server!\nServer Couldn't Be Found")
        