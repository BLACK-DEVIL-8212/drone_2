import os, socket,smtplib

def save_data():
    f = open("f{text}.txt","+r")
    f.write("data")
    pass

def connect_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Listening for connections on {host}:{port}...')

    while True:
        client_socket, client_address = server_socket.accept()
        message = client_socket.recv(1024).decode('utf-8')
        print(f'Message from client {client_address}: {message}')
        response = 'Hello, client!'
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

device_health()