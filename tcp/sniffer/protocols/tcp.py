from sniffer.protocols.protocol import Protocol
import itertools

class TCP(Protocol):
    header_format = '!HHIIBBHHH'
    header_length = 20
    header_fields = ["tcp_sport","tcp_dport","tcp_seq","tcp_ack","tcp_hlen","tcp_flag","tcp_window","tcp_chksum","tcp_urg"]

    def process(self,bytes_in):
        port_lookups = {80:'http', 443:'https', 22:'ssh'}
        super().process(bytes_in)
        self.parsed['tcp_flagstr'] = self.tcp_flags_as_str(self.parsed['tcp_flag'])
        self.parsed['tcp_sportstr'] = port_lookups.get(self.parsed['tcp_sport'])  
        self.parsed['tcp_dportstr'] = port_lookups.get(self.parsed['tcp_dport'])


    @staticmethod
    def tcp_flags_as_str(flag):
        file_flags = ['CWR',  'ECE', 'URG', 'ACK', 'PSH', 'RST', 'SYN', 'FIN']
        return "|".join(list(itertools.compress(file_flags,map(int,format(flag,"08b")))))
    