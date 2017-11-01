#!/usr/bin/python
from pwn import *
import time
import subprocess

f = open('breakpoints' ,'r')
commands = f.read()
f.close()

commands += 'run < input\n'
commands += 'python exec(open("commands.py").read())\n'

momo = process('./momo')
gdb.attach(momo, commands)

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
momo = subprocess.Popen(["./momo < flag"], stdout=subprocess.PIPE, shell=True)
out = momo.stdout.read()
if 'Congratulations!' in out:
    log.success('Flag found: %s', flag)
else:
    log.warning('Flag not found: %s', flag)
