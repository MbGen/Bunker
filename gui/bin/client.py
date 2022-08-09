import socket
import json
from pprint import pprint
import eel
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFF = 1024
DISCONNECT_MSG = "!DISCONNECT"
is_connected = False


def connect(ip, port):
    global is_connected
    try:
        client.connect((ip, port))
        eel.writeAlert(f"You are connected to {ip}")
        is_connected = True
        while True:
            data = client.recv(BUFF)
            player = json.loads(data.decode("utf-8"))
            pprint(player)
            time.sleep(2)
            # if input().lower() == "q":
            #     send(DISCONNECT_MSG)
            #     logger.info("Disconnecting")
            #     client.close()
            #     sys.exit()

    except ConnectionRefusedError:
        eel.writeAlert("Unable to connect")
        return
    except OSError:
        eel.writeAlert("There is no server with this ip and port")
        return


def send(msg: str):
    message = msg.encode("utf-8")
    client.send(message)


def connected():
    global is_connected
    return is_connected
