#!/usr/bin/python
#-*- coding: UTF-8 -*-
import gdb

flag = ''

options = {
	0:0,
	1:1,
	2:1,
	3:0,
	4:1,
	5:1,
	6:0,
	7:0,
	8:0,
	9:1,
	10:0,
	11:0,
	12:0,
	13:0,
	14:0,
	15:1,
	16:0,
	17:1,
	18:0,
	19:1,
	20:0,
	21:1,
	22:1,
	23:0,
	24:1,
	25:0
}
 
for i in range(0,28):
	if i == 17 or i == 26 or i == 27:
		flag += chr(int(gdb.parse_and_eval('$edx')))
		gdb.execute('c')
		gdb.execute('c')
	else: 
		b = int(gdb.parse_and_eval('$edx'))
		gdb.execute('c')
		a = int(gdb.parse_and_eval('$edx'))
		gdb.execute('c')
		if options[i] == 1: flag += chr(a+b)
		else: flag += chr(a-b)


f = open('flag.txt', 'w')
f.write(flag + '\n')
f.close()

gdb.execute('q')
