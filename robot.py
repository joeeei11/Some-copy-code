# -*- coding: utf-8 -*-

import threading
import socket
import platform

class robot():
    def __init__(self):
        self.locaddr = ('', 9000)  # (host, port)
        self.robotaddr = ('192.168.10.1', 8889)  # specified in manual
        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        print('socket binded')
        # recvThread create
        self.recvThread = threading.Thread(target=self.recv)
        self.recvThread.setDaemon(True)
        self.recvThread.start()
        print('Start receiving')

        # Need to send 'command' at first and recieve correct response(ok)
        self.send('command')

    def recv(self):
        while True:
            try:
                data, server = self.sock.recvfrom()
                print(data.decode(encoding="utf-8"))
            except Exception:
                print('Exit...')
                break

    def send(self, command):
        if 'end' in command:
            self.sock.sendto('stop'.encode(encoding="utf-8"), self.robotaddr)
            print('End robot...')
            self.sock.close()
        else:
            command = command.encode(encoding="utf-8")
            try:
                self.sock.sendto(command, self.robotaddr)
                print('Send {}'.format(command))
            except:
                print('counter except...')
                self.sock.close()

    def __del__(self):
        try:
            self.sock.sendto('stop'.encode(encoding="utf-8"), self.robotaddr)
        finally:
            self.sock.close()
            print('close socket')


### Testing
if __name__ == '__main__':
    host = ''
    port = 9000
    locaddr = (host, port)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    robot_address = ('192.168.10.1', )  # specified in manual

    sock.bind(locaddr)


    def recv():
        while True:
            try:
                data, server = sock.recvfrom()
                print(data.decode(encoding="utf-8"))
            except Exception:
                print('\nExit . . .\n')
                break


    print('\r\n\r\nrobot Python3 Demo.\r\n')

    print('robot: command forward back left right stop\r\n\
           Accelerate forward, backward, left or right?\r\n')

    print('end -- quit demo.\r\n')

    # recvThread create
    recvThread = threading.Thread(target=recv)
    recvThread.setDaemon(True)
    recvThread.start()

    while True:
        # Need to send 'command' at first and recieve correct response(ok)
        msg = 'command'.encode(encoding="utf-8")
        sent = sock.sendto(msg, robot_address)
        try:
            python_version = str(platform.python_version())
            version_init_num = int(python_version.partition('.')[0])

            if version_init_num == 3:
                msg = input("")
            elif version_init_num == 2:
                msg = input("")

            if not msg:
                break

            if 'end' in msg:
                print('...')
                sock.close()
                break

            # Send data
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, robot_address)
        except KeyboardInterrupt:
            print('\n . . .\n')
            sock.close()
            break