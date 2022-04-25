import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT=1234
myUsername = input("Username: ")

#creating socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting to interwebs
clientSocket.bind((IP,PORT))

#we do not want any message block
clientSocket.setblocking(False)

#putting usrrname together
username = myUsername.encode('utf-8')
usernameHeader = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
clientSocket.send(usernameHeader + username)

while True:
    message = input(f'{myUsername} > ') #> is the alignment
    if message:
        message = message.encode('utf-8')
        messageHeader = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        clientSocket.send(messageHeader+message)
        try:
            while True:
                usernameHeader = clientSocket.recv(HEADER_LENGTH)
                if not len(usernameHeader):
                    print("closed connection")
                    sys.exit()      #close the program
                usernameLength = int(usernameLength.decode('utf-8').strip())
                username = clientSocket.recv(usernameLength).decode('utf-8')
                
                messageHeader = clientSocket.recv(HEADER_LENGTH)
                messageLength = int(messageLength.decode('utf-8').strip())
                message = clientSocket.recv(messageLength).decode('utf-8')
                
                print(f'{username} > {message}')
        except IOError as e:
            print(e)
            continue
        except Exception as e:
            print(e)
            sys.exit()