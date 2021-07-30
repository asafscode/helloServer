import socket
import random
import sys
from datetime import datetime


def main():
    server.bind(("0.0.0.0", 4141))
    server.listen()
    while True:
        exited = False
        while not exited:
            (csocket, caddr) = server.accept()
            while not exited:
                lenData = csocket.recv(4)
                recvLen = int.from_bytes(lenData, "little")
                data = csocket.recv(recvLen)
                command = data.decode()
                if command == "Test":
                    reply = cmd_test()
                elif command == "Time":
                    reply = cmd_time()
                elif command == "Rand":
                    reply = cmd_rand()
                elif command == "Name":
                    reply = cmd_name()
                elif command == "Exit":
                    reply = cmd_exit()
                    exited = True
                else:
                    reply = "Unknown command!"
                reply = reply.encode()
                csocket.send(len(reply).to_bytes(4, byteorder="little"))
                csocket.send(reply)
            csocket.close()


def cmd_test():
    return "It works!"


def cmd_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def cmd_rand():
    random.seed()
    return str(random.randint(0, sys.maxsize))


def cmd_name():
    return "plz dont hack"


def cmd_exit():
    return "Bye!"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Closing server!")
        server.close()
