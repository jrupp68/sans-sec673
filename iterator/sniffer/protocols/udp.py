from sniffer.protocols.protocol import Protocol

class UDP(Protocol):
    header_format = '!HHHH'
    header_length = 8
    header_fields = ["udp_sport","udp_dport","udp_len","udp_chksum"]

    def __str__(self):
        return f"SPORT: {self.parsed['udp_sport']} DPORT: {self.parsed['udp_dport']}"