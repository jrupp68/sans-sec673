from sniffer.protocols.protocol import Protocol

class UDP(Protocol):
    header_format = '!HHHH'
    header_length = 8
    header_fields = ["udp_sport","udp_dport","udp_len","udp_chksum"]