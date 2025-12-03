import datetime
from collections import UserList
from sniffer.protocols import *

class Packet(UserList):

    def __init__(self, iterable=[]):
        if not isinstance(iterable, list):
            raise TypeError("Argument must be a list of Protocols")
        super().__init__()
        self.time = datetime.datetime.now()
        self.extend(iterable)

    def __str__(self):
        as_str = ""
        for position, protocol in enumerate(self):
             as_str += " + "*position + f"{protocol.name: <5} {str(protocol)}" + "\n"
        return as_str
      
    def __setitem__(self, pos, data):
        if not isinstance(data, Protocol):
            raise TypeError
        data.my_packet = self
        self.data.__setitem__(pos, data)

    def __add__(self,second_value):
        if isinstance(second_value, Protocol):
            return Packet([*self, second_value])
        elif isinstance(second_value, Packet):
            return Packet([*self, *second_value])
        return NotImplemented

    def __radd__(self, reflected_thing):
        if isinstance(reflected_thing, Protocol):
            return Packet([reflected_thing, *self])
        return NotImplemented

    def __getitem__(self, pos):
        if isinstance(pos, int):
            return self.data[pos]
        elif isinstance(pos, str):
            for eachlayer in self.data:
                if eachlayer.name == pos:
                    return eachlayer
            raise KeyError
        raise TypeError       

    def extend(self, iterable):
        for eachitem in iterable:
            self.append(eachitem)

    def insert(self, pos, data):
        if not isinstance(data, Protocol):
            raise TypeError("Packet can only contain Protocols")
        data.my_packet = self
        self.data.insert(pos, data)

    def append(self,data):
        if not isinstance(data, Protocol):
            raise TypeError("Packet can only contain Protocols")
        data.my_packet = self
        self.data.append(data)

    def from_bytes(self, data, no_ethernet = False):
        if not no_ethernet:
            #Process Ethernet Frame
            ethernet_frame = Ether(data, self)
            self.append(ethernet_frame)
            if hex(ethernet_frame.embedded_protocol) != "0x800":
                return 
            ip_data = ethernet_frame.raw_payload
        else:
            #First Frame is IP
            ip_data = data

        ip_frame = IP(ip_data, self)
        self.append(ip_frame)

        if ip_frame.embedded_protocol == "TCP":
            tcp_frame = TCP(ip_frame.raw_payload, self)
            self.append(tcp_frame)

        if ip_frame.embedded_protocol == "UDP":
            udp_frame = UDP(ip_frame.raw_payload, self)
            self.append(udp_frame)
        
        if ip_frame.embedded_protocol == "ICMP":
            icmp_frame = ICMP(ip_frame.raw_payload, self)
            self.append(icmp_frame)

