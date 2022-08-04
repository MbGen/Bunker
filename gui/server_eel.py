import eel
from datetime import datetime
from bin import server, client

eel.init('web')


@eel.expose
def start_server():
    eel.writeLog(f"{datetime.now().strftime(server.time_format)} Server is starting")
    server.start()


@eel.expose
def connect_server(ip_with_port: str):
    ip, port = ip_with_port.split(":")
    client.connect(ip, port)


eel.start('index.html', size=(400, 400), mode='edge')
