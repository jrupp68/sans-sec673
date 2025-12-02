from collections import UserList
from sniffer.protocols import Protocol

class Packet(UserList):
    
    def __init__(self, initlist=None):
        self.data = []
        if initlist:
            if type(initlist) == list():
                self.data.append(initlist)

    def __setitem__(self, pos, data):
        if type(data) != Protocol:
            print('Packet can only contains Protocols')
            raise TypeError
        self.data[pos] = data

    def append(self, data):
        if type(data) != Protocol:
            print('Packet can only contains Protocols')
            raise TypeError
        self.data.append(data)

    def extend(self, data):
        for item in data:
            if type(item) != Protocol:
                print('Packet can only contain Protocols')
                raise TypeError
            self.data.append(item)

    def insert(self, pos, data):
        if type(data) != Protocol:
            print('Packet can only contains Protocols')
            raise TypeError
        self.data.insert(pos, data)
