from operator import concat
import socket
import threading
import eel
from datetime import datetime
from loguru import logger
from .main import Player, Random


FORMAT = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
port = 32112
server.bind((ip, port))
BUFF = 4096
max_users = 1
DISCONNECT_MSG = "!DISCONNECT"
time_format = "%Y-%m-%d %H:%M:%S"

list_of_all_connections = []


def handle_client(conn: socket.socket, addr):
    eel.writeLog(f"{datetime.now().strftime(time_format)} User {addr} connected")
    list_of_all_connections.append(conn)
    connected = True
    while connected:
        try:
            msg = conn.recv(BUFF).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
        except ConnectionResetError:
            eel.writeLog(f"{datetime.now().strftime(time_format)} User {addr} disconnected")
            break
    conn.close()
    eel.writeLog(f"{datetime.now().strftime(time_format)} User {addr} disconnected")


def start():
    eel.writeLog(f"You hosted on {ip}:{port}")
    server.listen(max_users)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        eel.writeLog(f"{datetime.now().strftime(time_format)} "
                     f"Active connections {threading.active_count() - 1}/{max_users}")


def send_game_data_to_all():
    for connection in list_of_all_connections:
        try:
            connection.send(Player(**Random().generate_player_stats()).json().encode("utf-8"))
        except Exception as e:
            logger.error(e)
            continue
