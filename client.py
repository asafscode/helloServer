import socket


def main():
    print("connecting...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 420))
    exiting = False
    while not exiting:
        command = input("> ")
        if command == "Exit":
            exiting = True
        s.send(len(command).to_bytes(4, byteorder="little"))
        s.send(command.encode())
        respLen = int.from_bytes(s.recv(4), byteorder="little")
        resp = s.recv(respLen)
        print(resp.decode())
    s.close()
    exit(0)


if __name__ == '__main__':
    main()
