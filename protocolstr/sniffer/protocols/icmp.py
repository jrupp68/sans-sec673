from sniffer.protocols.protocol import Protocol


class ICMP(Protocol):
    header_format = "!BBH"
    header_length = 4
    header_fields = ["icmp_type", "icmp_code", "icmp_chksum"]

    def __str__(self):
        return f"Type: {self.parsed['icmp_type']} Code: {self.parsed['icmp_type']}"
