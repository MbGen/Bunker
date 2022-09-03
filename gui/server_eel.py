import eel
from datetime import datetime
from src import server, client
import threading


eel.init('web')

@eel.expose
def info():
    eel.writeAlert("В разработке")


@eel.expose
def start_server():
    thread = threading.Thread(target=server.start)
    thread.start()
    eel.writeLog(f"{datetime.now().strftime(server.time_format)} Server is starting")


@eel.expose
def connect_server(ip_with_port: str):
    try:
        ip, port = ip_with_port.split(":")
    except AttributeError:
        eel.writeAlert("Не удалось подключиться")
        return
    thread = threading.Thread(target=client.connect, args=(ip, int(port)))
    thread.start()


@eel.expose
def start_game():
    print("start sending")
    server.send_game_data_to_all()


@eel.expose
def is_connected() -> bool:
    eel.sleep(1)
    return client.is_connected


eel.start('index.html', size=(400, 400), mode='default')
