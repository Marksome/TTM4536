# Project - 0ctf_momo_3
0ctf\_momo\_3 is one of the reverse challenges from 0ctf 2016.

## Descriptions

#### Task description:  

#### Description of the problem:  

#### Description of the "angr" tool:  

#### Decription of the idea(s) for solution:  

#### Description of the specific functions used in the solution:  

## Workflow

#### Check filetype:  

#### Create dump file:  

#### Function addresses from dump:  

## Introduction to using the different tools  

#### Debugging:  
Using objdump, gdb or radare2 you can disassemble and find out how the program flow works. 

#### Using gdb:  
`gdb ./momo`  
Then you can use the different functions listed below.  
```
run
next
break <function> or *<address>
disassemble <function>
info <register, stack, etc.>
print <function>
x/<bytes>x $<pointer>
```  
To find the size of the stack compare the base pointer ($ebp) with the stack pointer ($esp).  
`x/2x $ebp`  
`x/64x $esp` 

#### Using radare2:
`r2 -AA ./momo`  
Then type vv and enter to visualize.  

#### Using python:
To enable running the program locally and connect through a socket, first create a new tab and type:  
`socat TCP-LISTEN:4536,reuseaddr,fork EXEC:"./momo"&`  

Then in the python script use:
```
#!/usr/bin/env python
import socket, telnetlib
sock = socket.socket()
sock.connect(('localhost', 4536))
t = telnetlib.Telnet()
t.sock = sock
t.interact()
``` 
Now you can interact directly because of telnetlib, and you can add things to the python script as you progress.

#### Using angr:
Basic setup:
```
#!/usr/bin/env python
import angr

def main():
	project = angr.Project("./momo")

if __name__ == '__main__':
    print main()
```  


