import sniffer.packet
import sniffer.protocols
import socket
import os
try:
    from rich.pretty import pprint
except:
    from pprint import pprint

def process_packet(data):
    new_packet = sniffer.packet.Packet()

    if os.name != "nt":
        #Windows can't sniff the ethernet layer
        ethernet_frame = sniffer.protocols.Ether(data)
        new_packet.append(ethernet_frame)
        if hex(ethernet_frame.embedded_protocol) != "0x800":
            return new_packet
        ip_data = ethernet_frame.raw_payload
    else:
        ip_data = data
    
    return new_packet

if __name__ == "__main__":
    protocols = {17:'UDP', 6:'TCP', 1:'ICMP'}

    if os.name == "nt":
        localhost = socket.gethostbyname(socket.gethostname())
        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        raw_socket.bind((localhost, 0))
        raw_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    else:
        raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    packets = []   
    while len(packets) < 1000:
        data = raw_socket.recv(65535)
        processed_packet = process_packet(data) 
        packets.append( processed_packet )
        for pos,layer in enumerate(processed_packet):
            print("--"*pos, layer)
            pprint(layer.parsed)
