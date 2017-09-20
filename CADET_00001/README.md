# Project - CADET_00001
CADET\_00001 is one of the challenge released by DARPA for the [Cyber Grand Challenge](https://github.com/CyberGrandChallenge/samples/tree/master/examples/CADET_00001).  

## Task description:  
This is an unusually simple service written by a military cadet as his first ever C program. It is intended as a data point as an incredibly simple service, with an incredibly simple vulnerability, written by an inexperienced programmer.  

The binary contains an easter egg and a stack buffer overflow.  

## Workflow
Check filetype:  
`file CADET\_00001.adapted`  
- ELF 32-bit LSB executable  

Create dump file: 
`objdump -d CADET\_00001.adapted > CADET\_00001.dump`

Function addresses from dump:
```
080484dd <transmit_all>
0804856c <receive_delim>
0804861e <transmit>
0804865c <receive>
0804872a <main>
08048808 <check>
```

Find segmentation fault:
`python -c "print 'a'*79" | ./CADET_00001.adapted`
```
Welcome to Palindrome Finder

        Please enter a possible palindrome: Segmentation fault
```
- This means that we can control the return address

Find Easter Egg:
`echo '^' | ./CADET_00001.adapted`
```
Welcome to Palindrome Finder

        Please enter a possible palindrome: 

EASTER EGG!

                Yes, that's a palindrome!
```


## Descriptions

### Description of the problem:  

###	Description of the "angr" tool:  

### Decription of the idea(s) for solution:  

### Description of the specific functions used in the solution:  

