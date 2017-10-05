#!/usr/bin/python
from pwn import *

f = open('b.gdb' ,'r')
commands = f.read()
f.close()

commands += 'python exec(open("commands.py").read())\n'

momo = process('./momo')
gdb.attach(momo, commands)
