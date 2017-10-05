#!/usr/bin/python
import sys
import string
import angr
from angr.block import CapstoneInsn, CapstoneBlock


ins_char = 0x81fe6e0
flag_char = 0x81fe6e4

after_fgets = 0x08049653
mov_congrats = 0x0805356E


def main():
    p = angr.Project('./momo', load_options={'auto_load_libs': False})

    addr = after_fgets
    size = mov_congrats - after_fgets

    # let's disasm with capstone to search targets
    insn_bytes = ''.join(
        p.loader.memory.read_bytes(addr, size))

    insns = []
    for cs_insn in p.arch.capstone.disasm(insn_bytes, addr):
        insns.append(CapstoneInsn(cs_insn))
    block = CapstoneBlock(addr, insns, 0, p.arch)

    targets = []

if __name__ == '__main__':
    print main()

