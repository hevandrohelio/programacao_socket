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

# função para lidar com o cliente
def handle_client(conn, name):
    while True:
        try:
            data = conn.recv(BUFFER_SIZE)

            if not data:
                break

            message = data.decode().strip()
            print(f"{name}: {message}")

            # broadcast
            for user, client_conn in users.items():
                try:
                    client_conn.send(f"{name}: {message}".encode())
                except:
                    pass

        except:
            break

    # cliente saiu
    print(f"{name} saiu")
    del users[name]
    conn.close()

while 1:
    conn, addr = server.accept() # conn = socket do cliente, addr = ip do cliente
    print("Conectado por: ", addr)

    name = conn.recv(BUFFER_SIZE).decode().strip()
    users[name] = conn
    print(f"{name} entrou no chat.")

    for client_conn in users.values():
        try:
            client_conn.send(f"{name} entrou no chat".encode())
        except:
            pass

    
    thread = threading.Thread(target=handle_client, args=(conn,name))
    thread.start()

server.close()