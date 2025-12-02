import struct
import codecs


class Protocol(object):
    header_format = None
    header_length = None
    header_fields = None

    def __init__(self, bytes = b"\x45"*50):
        assert self.header_fields != None, "Class requires a header_fields attribute."
        assert self.header_format != None, "Class requires a header_format attribute."
        assert self.header_length != None, "Class requires a header_length attribute."
        self.raw = bytes
        self.name = self.__class__.__qualname__
        self.embedded_protocol = "RAW"
        self.process(bytes)

    def process(self, bytes_in):
        assert isinstance(bytes_in, bytes), f"Expecting bytes as input got {type(bytes_in)}"
        self.unpacked = struct.unpack(self.header_format, bytes_in[:self.header_length])
        self.parsed = dict([(field,value) for field,value in zip(self.header_fields,self.unpacked)])
        self.raw_payload = bytes_in[self.header_length:]

    def __repr__(self):
        return f"{self.__class__.__qualname__}(header={codecs.encode(self.raw,'hex').decode()[:self.header_length]}, payload={self.raw_payload})"
    
    def __add__(self, second_value):
        from sniffer.packet import Packet
        if isinstance(second_value, Protocol):
            return Packet([self, second_value])
        else:
            return NotImplemented