import socket # responsável pela conexão TCP
import threading # aceita múltiplos clientes

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP

HOST = '127.0.0.1' # ip do servidor (local)
PORT = 24000 # porta
BUFFER_SIZE = 1024


# IP and port that server must wait for connect
server.bind((HOST, PORT))

server.listen()

print("Servidor disponível na porta 24000 e escutando...")
users={}
while 1:
    conn, addr = server.accept() # conn = socket do cliente, addr = ip do cliente
    print("Conectado por: ", addr)
    # função para lidar com o cliente
    def handle_client(conn):
        while True:
            data = conn.recv(BUFFER_SIZE)
            name = conn.recv(BUFFER_SIZE).decode().strip()

            if not data:
                break
            print(data.decode())

    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start