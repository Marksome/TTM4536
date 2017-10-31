#!/usr/bin/python
from pwn import *
import os

f = open('breakpoints' ,'r')
commands = f.read()
f.close()

commands += 'run < input\n'
commands += 'python exec(open("commands.py").read())\n'


log.info('Starting reverse engineering...')
momo = process('./momo')
gdb.attach(momo, commands)
log.info('Reverse engineering done...')

log.info('Running program with input "flag":')
os.system("./momo < flag")

f = open('flag', 'r')
flag = f.read()
f.close()

log.info('Flag found: %s', flag)
