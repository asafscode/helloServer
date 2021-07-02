import socket
import random
import sys
from datetime import datetime


def main():
    server.bind(("0.0.0.0", 420))
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
                    reply = "It works!"
                elif command == "Time":
                    reply = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                elif command == "Rand":
                    random.seed()
                    reply = str(random.randint(0, sys.maxsize))
                elif command == "Name":
                    reply = "plz dont hack"
                elif command == "Exit":
                    reply = "Bye!"
                    exited = True
                else:
                    reply = "Unknown command!"
                reply = reply.encode()
                csocket.send(len(reply).to_bytes(4, byteorder="little"))
                csocket.send(reply)
            csocket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Closing server!")
        server.close()
