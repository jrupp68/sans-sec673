from sniffer.protocols import *
from sniffer.packet import Packet

pkt = Packet([ Ether() , IP() , TCP()])
a = pkt[0].SRC_MAC
b = pkt[0].encapsulated