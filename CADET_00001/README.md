# Project - CADET_00001
CADET\_00001 is one of the challenge released by DARPA for the [Cyber Grand Challenge](https://github.com/CyberGrandChallenge/samples/tree/master/examples/CADET_00001).  

## Task description:  
This is an unusually simple service written by a military cadet as his first ever C program. It is intended as a data point as an incredibly simple service, with an incredibly simple vulnerability, written by an inexperienced programmer.  

The binary contains an easter egg and a stack buffer overflow.  

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

#### Debugging:
Using objdump, gdb or radare2 you can disassemble and find out how the program flow works. 


#### Using radare2:
`r2 -AA CADET_00001.adapted`
Then type v, then v and enter to visualize.
Here we can see two intesting addresses we would like to try with angr.
```
0x080487ac      mov dword [esp + local_4h], str._t_tNope__that_s_not_a_palindrome_n_n
0x080487d8      mov dword [esp + local_4h], str._t_tYes__that_s_a_palindrome__n_n
```

#### Using angr:
To try and explore the two addresses shown above we use angr with its function explore.
`ex = p.surveyors.Explorer(find=(0x080487d8,), avoid=(0x080487ac,))`


## Descriptions

#### Description of the problem:  

#### Description of the "angr" tool:  

#### Decription of the idea(s) for solution:  

#### Description of the specific functions used in the solution:  

