#!/usr/bin/env python3

import socket
import datetime
import signal
import sys

def signal_handler(sig, frame):
    print("\nСервер завершает работу.")
    sys.exit(0)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1303))
    server_socket.listen(1)

    print("Сервер запущен. Ожидание подключений...")

    while True:
        try:
            connection, address = server_socket.accept()
            print(f"Подключено клиент: {address}")

            current_time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            connection.sendall(current_time.encode('utf-8'))

            connection.close()
            print(f"Отправлено время: {current_time}\nОжидание нового подключения...")
        except KeyboardInterrupt:
            server_socket.close()
            print("\nСервер завершает работу.")
            sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    start_server()
