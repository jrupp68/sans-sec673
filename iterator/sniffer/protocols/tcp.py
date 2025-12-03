from sniffer.protocols.protocol import Protocol

class TCP(Protocol):
    header_format = '!HHIIBBHHH'
    header_length = 20
    header_fields = ["tcp_sport","tcp_dport","tcp_seq","tcp_ack","tcp_hlen","tcp_flag","tcp_window","tcp_chksum","tcp_urg"]

    def __str__(self):
        return f"SPORT: {self.parsed['tcp_sport']} DPORT {self.parsed['tcp_dport']} Flags {self.parsed['tcp_flag']}"