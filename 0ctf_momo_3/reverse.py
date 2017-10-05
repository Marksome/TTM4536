#!/usr/bin/python
from pwn import *

f = open('breakpoints' ,'r')
commands = f.read()
f.close()

commands += 'python exec(open("commands.py").read())\n'

momo = process('./momo')
gdb.attach(momo, commands)
