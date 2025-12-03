from sniffer.protocols.protocol import Protocol
import codecs

class Ether(Protocol):
    header_format = '!6s6sH'
    header_length = 14
    header_fields = ["SRC_MAC","DST_MAC","ETYPE"]

    def process(self, bytes_in):
        super().process(bytes_in)
        self.parsed['SRC_MAC'] = codecs.encode(self.parsed['SRC_MAC'],"hex")
        self.parsed['DST_MAC'] = codecs.encode(self.parsed['DST_MAC'],"hex")
        self.embedded_protocol = self.parsed['ETYPE']

    def __str__(self):
        nice_src = ':'.join([self.parsed['SRC_MAC'].decode()[x:x+2] for x in range(0,12,2)])
        nice_dst = ':'.join([self.parsed['DST_MAC'].decode()[x:x+2] for x in range(0,12,2)])
        return f"{nice_src} > {nice_dst} Ethernet Type {self.parsed['ETYPE']}"


