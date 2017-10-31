#!/usr/bin/python
from pwn import *
import time
import os

f = open('breakpoints' ,'r')
commands = f.read()
f.close()

commands += 'run < input\n'
commands += 'python exec(open("commands.py").read())\n'

log.info('Starting reverse engineering...')
momo = process('./momo')
gdb.attach(momo, commands)
log.success('Reverse engineering done...')

read = False
while not read:
    try:
        f = open('flag', 'r')
        flag = f.read()
        f.close()
        read = True
    except:
        time.sleep(0.5)

log.info('Running program with input "flag":')
os.system("./momo < flag")

log.success('Flag found: %s', flag)
