# Create your TCP class here.

# You can use a header format of '!HHIIBBHHH'
# The correct header length is 20
# The TCP Header field names are ["tcp_sport","tcp_dport","tcp_seq","tcp_ack","tcp_hlen","tcp_flag","tcp_window","tcp_chksum","tcp_urg"]

# You can use this port lookup table for the tcp_sportstr and tcp_dportstr fields
port_lookups = {80:'http', 443:'https', 22:'ssh'}

#You can convert this function taken from the 573 sniffer into a method and use it to convert tcp_flags to a string.
# def tcp_flags_as_str(flag):
#     file_flags = ['CWR',  'ECE', 'URG', 'ACK', 'PSH', 'RST', 'SYN', 'FIN']
#         return "|".join(list(itertools.compress(file_flags,map(int,format(flag,"08b")))))




