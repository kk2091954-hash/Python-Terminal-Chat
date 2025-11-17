from socket import *


def start_server():
    server_socket  = socket(AF_INET, SOCK_STREAM)
    server_address = ('127.0.0.1', 443)

    server_socket.bind(server_address)
    server_socket.listen(1)

    print(f'[SERVER] Waiting for connection on {server_address[0]}:{server_address[1]}')

    client_socket, client_addr = server_socket.accept()
    print(f'[SERVER] Connected with {client_addr}')

    try:
        while True:
            # send message to client
            server_msg = input('Server: ')
            client_socket.send(server_msg.encode('utf-8'))

            # receive message from client
            client_msg = client_socket.recv(1024)
            if not client_msg:
                print('[SERVER] Client disconnected')
                break
            print('Client:', client_msg.decode('utf-8'))

    except KeyboardInterrupt:
        print('\n[SERVER] Closed manually')

    finally:
        client_socket.close()
        server_socket.close()
        print('[SERVER] Connection closed')


if __name__ == '__main__':
    start_server()