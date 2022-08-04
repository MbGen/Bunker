import socket
import json
import sys
from pprint import pprint
from loguru import logger
import eel


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFF = 1024
DISCONNECT_MSG = "!DISCONNECT"


def connect(ip, port):
    try:
        client.connect((ip, port))
        eel.writeAlert(f"You are connected to {ip}")
    except ConnectionRefusedError:
        eel.writeAlert("There is no server with this ip and port")
        sys.exit()

    while True:
        if input().lower() == "q":
            send(DISCONNECT_MSG)
            logger.info("Disconnecting")
            client.close()
            sys.exit()
        data = client.recv(BUFF)
        player = json.loads(data.decode("utf-8"))
        pprint(player)


def send(msg: str):
    message = msg.encode("utf-8")
    client.send(message)
