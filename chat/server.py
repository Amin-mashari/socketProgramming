import socket ,  threading


'chat room connection : client to client TCP connection'
 
host = "127.0.0.1"
port = 30809

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
users = []
def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = users[index]
            broadcast(f'{username} has left the chat room!\n'.encode('utf-8'))
            users.remove(username)

            break

def receive():
    while True:
        print('Server id running and listening\n')
        client , address = server.accept()
        print(f'connection is established with {str(address)}\n')
        client.send('username?'.encode('utf-8'))
        username = client.recv(1024)
        users.append(username)
        clients.append(client)

        print(f'the name of this client is : {username}'.encode('utf-8'))
        broadcast(f'{username} has connected to the chat room'.encode('utf-8'))
        client.send('you are connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client , args=(client, ))
        thread.start()

if __name__ == '__main__':
    receive()