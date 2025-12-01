import sys


class CustomInt(int):
    def __add__(self,newval):
        total = 0
        for _ in range(self):
            total += 1
        for _ in range(newval):
            total += 1
        return total

def add(a,b):
    return a+b

def addmany(*args):
    return sum(args)

def bytes_to_str(inb):
    return inb.decode()

def str_to_bytes(ins):
    return ins.encode()

def byte_length(ins):
    return len(ins.encode())
