#!/usr/bin/python
from pwn import *
import os
import subprocess 

f = open('breakpoints' ,'r')
commands = f.read()
f.close()

commands += 'python exec(open("commands.py").read())\n'


log.info('Starting reverse engineering...')
momo = process('./momo')
gdb.attach(momo, commands)
momo.wait()
log.info('Reverse engineering done...')

log.info('Running program with input "flag":')
os.system("./momo < flag")

f = open('flag', 'r')
flag = f.read()
f.close()

log.info('Flag found: %s', flag)
