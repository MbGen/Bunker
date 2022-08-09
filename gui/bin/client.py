import socket
import json
from pprint import pprint
import eel
import time
from .main import Player


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFF = 1024
DISCONNECT_MSG = "!DISCONNECT"


def connect(ip, port):
    try:
        client.connect((ip, port))
        eel.writeAlert(f"You are connected to {ip}")
        is_connected = True
        while True:
            data = client.recv(BUFF)
            player = json.loads(data.decode("utf-8"))
            player = Player(**player) 
            eel.showPlayer(player)
    except ConnectionRefusedError:
        eel.writeAlert("Unable to connect")
        return
    except OSError:
        eel.writeAlert("There is no server with this ip and port")
        return


def send(msg: str):
    message = msg.encode("utf-8")
    client.send(message)
