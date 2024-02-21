import socket
import threading
import sys
from queue import Queue
from pathlib import Path

try:
    a1 = sys.argv[1]
    if a1.startswith('https://'):
        a1 = a1[8:]
    else:
        a1 = a1
except IndexError:
    # print(e)
    a1 = 'www.google.com'

target = a1
# target = '10.1.8.27'
portscan_socket_timeout = 5

def portscan(port):
    # print("port p pp p p pp p pp ")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(portscan_socket_timeout)
        sock.connect((target, port))
        sock.close()
        # print(port, "hello")
        return True
    except OSError:
        # print(port, "hello")
        return False


# noinspection PyShadowingNames
def fill_queue(port_list):
    # print("fill q")
    for port in port_list:
        q.put(port)
        # print(port)


def worker():
    while not q.empty():
        port = q.get()
        if portscan(port):
            print("port", port, "is open")
            open_ports.append(port)
        q.task_done()


q = Queue()
open_ports = []
port_list = []


def fill_port_list(from1, to1):
    global port_list
    for i in range(from1, to1):
        port_list.append(i)


# fill_port_list(2, 81)
# fill_queue(port_list)
# print(port_list)


def portscanner(thread1, a, b):
    global thread_list
    fill_port_list(a, b)
    fill_queue(port_list)
    print('\n\n Starting Port Scanning...\n\n ')
    print(f"thread={thread1}")
    print(f" target={target}")
    for i in range(1, thread1):
        threading.Thread(target=worker).start()

    q.join()

    a1 = target.replace("http://", "").replace("www.", "").replace("https://", "")
    # Remove invalid characters from the target
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        a1 = a1.replace(char, '_')
    print(f"open ports:{open_ports}")

    path = Path(f"result/{a1}")
    path.exists() or path.mkdir(parents=True)
    with (path / 'port.txt').open('w+') as f:
        f.write(f"open ports:{open_ports}")

    return 0


if __name__ == '__main__':
    portscanner(111, 3, 99)

