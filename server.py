import socket
import sys
import select

recv_b = 4096
server_list = []

#host = socket.gethostname()
#port = int(input("Enter your port Number: "))
def broadcast(s,sock,message):
    for socket in server_list:
        if socket != s and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                if socket in server_list:
                    server_list.remove(socket)
def server_connexion():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = int(input("Enter your Port Number: "))
    print("HostName " + host)
    if port >= 36758:
        print("this port Number is out of range use another one\nRestart Your application and use a valid Range PORT")
    else:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host,port))
        s.listen(10)
        conn , addr = s.accept()

        print("Got connexion from {0} using port {1}".format(addr[0],addr[1]))

        #while True:
          #  data = conn.recv(1024)
           # if not data: break
           # conn.sendall(data)
        server_list.append(s)
        while 1:
            redy_to_read, ready_to_write, in_error = select.select(server_list,[],[],0)
            for sock in redy_to_read:
                if sock == s:
                    socknew, addr = s.accept()
                    server_list.append(socknew)
                    print("New User(%s, %s) connected "%addr)
                    broadcast(s,socknew,"[%s:%s] entered our Quizz game\n"%addr)
                    #new message new answer
                else:
                    try:
                        #receive an answer from a socket.
                        data = sock.recv(recv_b)
                        if data:
                            #received a value
                            broadcast(s,sock,"\r"+ "[" + str(sock.getpeername()) + "]" + data )
                        else:
                            #remove that socket which is broken
                            if sock in server_list:
                                server_list.remove(sock)
                            #no data = broken connexion
                            broadcast(s, sock, "Client (%s, %s) is offline\n" %addr)
                    except:
                        broadcast(s,sock,"Client (%s, %s) is offline\n" %addr)
                        continue
                        
    s.close()

if __name__ == "__main__" :
    sys.exit(server_connexion())
try:
    server_connexion()
except:
    print("Soit le port est deja en utilisation \nSoit D'autres erreurs sont dans votre connexion")

