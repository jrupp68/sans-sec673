#!/usr/bin/env python3
import sys

def add(a,b):
    return a + b


def addmany(*allnums):
    return (sum(allnums))


def bytes_to_str(inbytes:bytes) -> str:
    return inbytes.decode()


def str_to_bytes(instr:str) -> bytes:
    return instr.encode()


def byte_length(utr8_char:str) -> int:
    as_bytes = utr8_char.encode()
    return len(as_bytes)

if __name__ == '__main__':
    total = 0.0
    for each_arg in sys.argv[1:]:
        try:
            total += float(each_arg)
        except:
            pass
    print(total)