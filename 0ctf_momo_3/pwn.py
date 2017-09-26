from pwn import *

gdb.attach('bash')
bash = process('bash')

gdb.attach(bash, '''
        set follow-fork-mode child
        break execve
        continue
        ''')

bash.sendline('whoami')
