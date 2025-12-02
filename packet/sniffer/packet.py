from collections import UserList
from sniffer.protocols import Protocol

class Packet(UserList):
    
    def __init__(self, iterable=[]):
        super().__init__(self)
        self.extend(iterable)

    def extend(self, iterable):
        for val in iterable:
            self.append(val)

    def append(self, val):
        if not isinstance(val,Protocol):
            raise TypeError
        self.data.append(val)

    def __setitem__(self, pos, val):
        if not isinstance(val,Protocol):
            raise TypeError
        self.data[pos] = val

    def insert(self, pos, val):
        if not isinstance(val,Protocol):
            raise TypeError
        self.data.insert(pos, val)
