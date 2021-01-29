import socket
host = socket.gethostname()
port = int(input("Enter a Specific Port Number (Avoid using used port Numbers) =>"))
try:
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    print('Got connection from ', addr[0], '(', addr[1], ')')
    print('Thank you for connecting ' + addr[0])
    while True:
        data = conn.recv(1024)
        if not data: break
    conn.sendall(data)
    conn.close()
except OSError:
    print("This port Number is already taken. Try to use a different port Number")
    print("App is restarting")
except ValueError:
    print("the value entered can't be used to get a connexion")