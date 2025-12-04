from sniffer.protocols.protocol import Protocol
import struct
import socket

class IP(Protocol):
    header_format = '!BBHHHBBHLL'
    header_length = 20
    header_fields = ["ip_byte0", "ip_svc", "ip_total_len","ip_id","ip_frag","ip_ttl","ip_proto","ip_chksum","ip_src","ip_dst"]

    def process(self,bytes_in):
        protocols = {17:'UDP', 6:'TCP', 1:'ICMP'}
        super().process(bytes_in)
        #Make IP Address look like an IP address
        self.parsed["ip_src"] = socket.inet_ntoa(struct.pack('!I',self.parsed["ip_src"]))
        self.parsed["ip_dst"] = socket.inet_ntoa(struct.pack('!I',self.parsed["ip_dst"]))
        #Calculate header length
        ip_header_length = (self.parsed["ip_byte0"] & 15)  * 4
        ip_options_length = ((ip_header_length-20 + 3 ) // 4) *4
        self.embedded_protocol = protocols.get(self.parsed["ip_proto"],"UNKNOWN")
        #Handle IP Options if there are any
        if ip_options_length:
            structstring = "!{0}s".format(ip_options_length)
            self.parsed["ip_options"] = struct.unpack(structstring, self.raw[34:34+ip_options_length])
            self.raw_payload = self.raw_payload[ip_options_length:]

    def __str__(self):
        return f"{self.parsed['ip_src']} > {self.parsed['ip_dst']} Protocol {self.embedded_protocol}"