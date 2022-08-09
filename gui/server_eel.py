import eel
from datetime import datetime
from bin import server, client
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
    ip, port = ip_with_port.split(":")
    client.connect(ip, int(port))


@eel.expose
def start_game():
    print("start sending")
    server.send_game_data_to_all()


eel.start('index.html', size=(400, 400), mode='default')
