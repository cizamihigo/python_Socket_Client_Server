import socket
import sys
import select

client_list = []
def connect_cleint():
    if(len(sys.argv) < 3):
        print("Usage: python client.py hostname port name")
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)

    print("trying to connect a remote host .  .  . ")
    try:
        
        s.connect((host,port))
    except:
        print("Was Unable to Connect")
        sys.exit()
    print("Can start the Game Cause connected to a remote sever")
    sys.stdout.write('[Me]'); sys.stdout.flush()

    #client_list.append(sys.stdin)

    while 1:
        #s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        client_list = [sys.stdin, s]
        #readble sockets
        read_sockets, write_sockets, errors_socket = select.select(client_list[0], [], [], 0)
        for sock in read_sockets:
            if sock == s:

                #Coming message from server
                data = sock.recv(4096)
                if not data :
                    print("\nDisconnected from server")
                    sys.exit()
                else:
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me]');sys.stdout.flush()
            else:
                #enter the game answer
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me]');sys.stdout.flush()

if __name__ == "__main__":
    sys.exit(connect_cleint())
#connect_cleint()


