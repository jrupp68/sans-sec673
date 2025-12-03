import struct
import codecs


class Protocol(object):
    header_format = None
    header_length = None
    header_fields = None


    def __init__(self, bytes = b"\x45"*50, packet = None):
        assert self.header_fields != None, "Class requires a header_fields attribute."
        assert self.header_format != None, "Class requires a header_format attribute."
        assert self.header_length != None, "Class requires a header_length attribute."
        self.raw = bytes
        self.name = self.__class__.__qualname__
        self.embedded_protocol = "RAW"
        self.process(bytes)
        self.my_packet = packet


    def process(self, bytes_in):
        assert isinstance(bytes_in, bytes), f"Expecting bytes as input got {type(bytes_in)}"
        self.unpacked = struct.unpack(self.header_format, bytes_in[:self.header_length])
        self.parsed = dict([(field,value) for field,value in zip(self.header_fields,self.unpacked)])
        self.raw_payload = bytes_in[self.header_length:]

    def __repr__(self):
        return f"{self.__class__.__qualname__}(header={codecs.encode(self.raw,'hex').decode()[:self.header_length]}, payload={self.raw_payload})"

    def __add__(self, otherthing):
        from sniffer.packet import Packet
        if isinstance(otherthing, Protocol):
            return Packet([self,otherthing])
        return NotImplemented

    def __getattr__(self, name):
        if name in self.parsed:
            return self.parsed.get(name)
        raise AttributeError(f"{self.name} has no attribute {name}")

    @property
    def encapsulator(self):
        assert self.my_packet != None, "Lonely Packet"
        # I'm in the start of the list, can't go up
        if self.my_packet[0] == self:
            return None
        index = self.my_packet.index(self)
        return self.my_packet[index - 1]
    
    @property
    def encapsulated(self):
        # return protocol direclty after this protocol in the same packet

        # check if this is actualy in a packet
        assert self.my_packet != None, "Lonely Packet"

        # check if this is at the end of the list can't go down
        if self.my_packet[-1] == self:
            return None

        # get index of self in the packet
        index = self.my_packet.index(self)

        # return the protocol following
        return self.my_packet[index + 1]

    
