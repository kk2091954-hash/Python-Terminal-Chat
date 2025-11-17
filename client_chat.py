import time
from socket import *


def start_client():
    client_socket  = socket(AF_INET, SOCK_STREAM)
    server_address = ('127.0.0.1', 443)

    print(f'[CLIENT] Trying to connect to {server_address[0]}:{server_address[1]}')

    # keep trying to connect if server not started yet
    while True:
        try:
            client_socket.connect(server_address)
            print('[CLIENT] Connected to server')
            break
        except:
            print('[CLIENT] Server not available... retrying')
            time.sleep(1)

    try:
        while True:
            # receive message from server
            server_msg = client_socket.recv(1024)
            if not server_msg:
                print('[CLIENT] Server disconnected')
                break
            print('Server:', server_msg.decode('utf-8'))

            # send message to server
            client_msg = input('Client: ')
            client_socket.send(client_msg.encode('utf-8'))

    except KeyboardInterrupt:
        print('\n[CLIENT] Closed manually')

    finally:
        client_socket.close()
        print('[CLIENT] Connection closed')


if __name__ == '__main__':
    start_client()