from collections import UserList
from sniffer.protocols import *

class Packet(UserList):
      
    def __setitem__(self, pos, data):
        if not isinstance(data, Protocol):
            raise TypeError
        self.data.__setitem__(pos, data)

    def __init__(self, iterable=[]):
        if not isinstance(iterable, list):
            raise TypeError("Argument must be a list of Protocols")
        super().__init__()
        self.extend(iterable)

    def extend(self, iterable):
        for eachitem in iterable:
            self.append(eachitem)

    def insert(self, pos, data):
        if not isinstance(data, Protocol):
            raise TypeError("Packet can only contain Protocols")
        self.data.insert(pos, data)

    def append(self,data):
        if not isinstance(data, Protocol):
            raise TypeError("Packet can only contain Protocols")
        self.data.append(data)
