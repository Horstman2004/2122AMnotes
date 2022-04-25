import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT=1234

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#help deal when we have 2 address being used
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

serverSocket.bind((IP,PORT))
serverSocket.listen()
print(f'Listening for connections on {IP}:{PORT}...')

#dictionary
clients={}
#list of all of the sockets
socketsList = [serverSocket]

def reciveMessage(clientSocket):
    #try to do this
    try:
        messageHeader = clientSocket.recv(HEADER_LENGTH)
        print(messageHeader)
        #check if client loses connection
        if not (len(messageHeader)):
            return True
        messageLength = int(messageHeader.decode('utf-8').strip())
        return{'header':messageHeader,'data':clientSocket.recv(messageLength)}
    except:
        #if not good,
        return False

while True:
    readSocket, _,excepttionSocket = select.select(socketsList,[],socketsList)
    
    for notifiedSocket in readSocket:
        #if the notified socket s our server socket, we have a new connection
        if notifiedSocket == serverSocket:
            clientSocket,clientAddress = serverSocket.accept()
            user = reciveMessage(clientSocket)
            if user is False:
                continue
            socketsList.append(clientSocket)
            clients[clientSocket]=user
            print('Accepted new connection from {}:{}, username: {}'.format(clientAddress,user['data'].decode('utf-8')))
        #else we have an old connection or a new message
        else:
            message = reciveMessage(notifiedSocket)
            if message is False:
                print('CLosed Connection from: {}'.format(clients[notifiedSocket]['data'].decode('utf-8')))
                socketsList.remove[notifiedSocket]
                del clients[notifiedSocket]
                continue
            #now proces the new message
            user = clients[notifiedSocket]
            print(f'Recived message from {user["data"].decode("utf-8")}')
            print(f'\t{message["data"].decode("utf-8")}')
            
            for clientSocket in clients:
                if clientSocket != notifiedSocket:
                    clientSocket.send(user['header']+user['data']+message['header']+message['data'])
                
                