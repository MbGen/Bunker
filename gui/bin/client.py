import socket
import json
from pprint import pprint
import eel
from .main import Player


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFF = 4096
DISCONNECT_MSG = "!DISCONNECT"
is_connetced = False


def connect(ip, port):
    global is_connected
    try:
        client.connect((ip, port))
        eel.writeAlert(f"You are connected to {ip}")
        is_connected = True
        while True:
            data = client.recv(BUFF)
            player = json.loads(data.decode("utf-8"))
            eel.showPlayer(player)
    except ConnectionRefusedError:
        is_connected = False
        eel.writeAlert("Unable to connect")
        return
    except OSError:
        is_connected = False
        eel.writeAlert("There is no server with this ip and port")
        return


def send(msg: str):
    message = msg.encode("utf-8")
    client.send(message)


def is_connected() -> bool:
    "returns: status of current connection"
    global is_connected
    return is_connected
