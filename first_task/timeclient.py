#!/usr/bin/env python3

import socket

def connect_to_server():
    server_ip = input("Введите IP адрес сервера: ")
    server_address = (server_ip, 1303)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)
        received_data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено время с сервера: {received_data}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    connect_to_server()

