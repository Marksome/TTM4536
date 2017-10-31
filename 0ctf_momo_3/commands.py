#!/usr/bin/python
#-*- coding: UTF-8 -*-
import gdb

flag = ''

for i in range(0,27):
	before = int(gdb.parse_and_eval('$eax'))
	b = int(gdb.parse_and_eval('$edx'))
	gdb.execute('c')
	after = int(gdb.parse_and_eval('$eax'))
	a = int(gdb.parse_and_eval('$edx'))
	gdb.execute('c')
	if a == b:
		flag += chr(a)
	elif before > after:
		flag += chr(a+b)
	elif before < after:
		flag += chr(a-b)


flag += chr(int(gdb.parse_and_eval('$edx')))

f = open('flag', 'w')
f.write(flag + '\n')
f.close()

gdb.execute('q')
