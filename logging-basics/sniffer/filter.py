import ipaddress

from sniffer.packet import Packet
from sniffer.protocols import *


class Filter(object):
    def __init__(self, protocol, field, value):
        if not isinstance(protocol, str):
            raise TypeError("The protocol must be a string")
        if not isinstance(field, str):
            raise TypeError("The field must be a string")
        if protocol == "IP":
            if field in ["ip_src","ip_dst"]:
                value = self.addr_to_list(value)            
        self.protocol = protocol
        self.field = field
        self.value = value

    @staticmethod
    def addr_to_list( addr ):
        if "/" in addr:
            return list(map(str, ipaddress.ip_network( addr , strict=False)))
        else:
            return [ addr ]

    def __eq__(self, other):
        if isinstance(other, Protocol):
            raise TypeError("Filters are compared to Packets not Protocols.")
        if isinstance(other,list):
            for eachlayer in other:
                if eachlayer.name == self.protocol:
                    layer = eachlayer
                    break
            else:
                return False
            myval = getattr( layer, self.field, "NOT FOUND")
            if myval == "NOT FOUND":
                return False
            if isinstance(self.value, list):
                return myval in self.value
            return myval == self.value
        return NotImplemented

    def __repr__(self):
        return f"Filter(protocol='{self.protocol}', field='{self.field}', value = {self.value})"


