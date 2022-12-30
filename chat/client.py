import time, socket, threading

username = input("pick a username >>> ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1' ,30809 ))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "username?":
                client.send(username.encode('utf-8'))
            else:
                print(message+"\n")
        except:
                print('Error!\n')
                client.close()
                break

def client_send():
    while True:
        t = time.strftime('%H:%M', time.localtime())
        message = f'{t}:{username} >> {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()