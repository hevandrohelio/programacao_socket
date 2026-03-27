import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criação do socket TCP

HOST = '127.0.0.1'
PORT = 24000
BUFFER_SIZE = 1024

client.connect((HOST, PORT)) # abre a conexão TCP com o servidor

name = input("Digite seu nome de usuário: ")
client.send(name.encode()) # string -> bytes  e envia pro servidor

def receive_messages():
    while True: # escuta as mensagens
        try:
            data = client.recv(BUFFER_SIZE) # espera
            if not data:
                break
            print(data.decode()) # bytes -> strings
        except: # encerra se conexão cair
            break

def send_messages():
    while True:
        message = input()
        client.send(message.encode())

# iniciando as threads
thread_receive = threading.Thread(target=receive_messages)
thread_send = threading.Thread(target=send_messages)

thread_receive.start()
thread_send.start()