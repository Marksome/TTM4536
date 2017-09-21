# Project - CADET_00001
CADET\_00001 is one of the challenge released by DARPA for the [Cyber Grand Challenge](https://github.com/CyberGrandChallenge/samples/tree/master/examples/CADET_00001).  

## Descriptions

#### Task description:  
This is an unusually simple service written by a military cadet as his first ever C program. It is intended as a data point as an incredibly simple service, with an incredibly simple vulnerability, written by an inexperienced programmer.  

The binary contains an easter egg and a stack buffer overflow.  

#### Description of the problem:  
The stack of the program has 64 bytes allocated, the problem is that it reads 128 bytes at a time.  
This means the stack can be overflowed and the extra data will overwrite other functions and variables.  

#### Description of the "angr" tool:  
`angr` is a powerful tool if you have little to no understanding of how the executable works, or don't have the source code.  
`angr` has the ability to give a control-flow analysis, data-dependency analysis, symbolic execution and program instrumentation.  
`angr` can also search for ways to reach an address and try to avoid others.  
In this project symbolic execution and data-dependency analysis will be used.  

#### Decription of the idea(s) for solution:  
In buffer overflows we feed the program with more and more data untill we receive a segmentation fault or another error. The goal is to overwrite the return address or instruction pointer. For finding the easter egg, we could brute force or disassemble and reverse engineer the program. 

#### Description of the specific functions used in the solution:  
To disassemble and analyse the executable I used gdb-peda and radare2. 
In the first solution I used bash to find the segmentation fault and the easter egg.  
In the second solution I used python to transmit the data through a socket.  
In the third solution I used python with angr to 

## Workflow

#### Check filetype:  
`file CADET\_00001.adapted`  
- ELF 32-bit LSB executable  

#### Create dump file:  
`objdump -d CADET\_00001.adapted > CADET\_00001.dump`

#### Function addresses from dump:  
```
080484dd <transmit_all>
0804856c <receive_delim>
0804860d <_terminate>
0804861e <transmit>
0804865c <receive>
0804872a <main>
08048808 <check>
```

#### Find segmentation fault:  
`python -c "print 'a'*79" | ./CADET_00001.adapted`
```
Welcome to Palindrome Finder
        Please enter a possible palindrome: Segmentation fault
```
This means that a segmentation fault happened and something important was written over. 

#### Find Easter Egg:
`echo '^' | ./CADET_00001.adapted`
```
Welcome to Palindrome Finder
        Please enter a possible palindrome: 
EASTER EGG!
                Yes, that's a palindrome!
```

## Introduction to using the different tools  

#### Debugging:  
Using objdump, gdb or radare2 you can disassemble and find out how the program flow works. 

#### Using gdb:  
`gdb ./CADET_00001.adapted`  
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
`r2 -AA CADET_00001.adapted`  
Then type vv and enter to visualize.  
Here we can see two intesting addresses we would like to try with angr.
```
0x080487ac      mov dword [esp + local_4h], str._t_tNope__that_s_not_a_palindrome_n_n
0x080487d8      mov dword [esp + local_4h], str._t_tYes__that_s_a_palindrome__n_n
```

#### Using python:
To enable running the program locally and connect through a socket, first create a new tab and type:  
`socat TCP-LISTEN:4536,reuseaddr,fork EXEC:"./CADET_00001.adapted"&`  

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
	project = angr.Project("./CADET_00001.adapted")

if __name__ == '__main__':
    print main()
```  
To try and explore the find and avoid the addresses found in debugging we can use angr with its function 'explorer'.  
`explorer = project.surveyors.Explorer(find=(0x080487d8,), avoid=(0x080487ac,))`  

