import time
import os
import socket
import string


def linux_send(raw_bytes, interface="lo"):
    "This method accepts raw bytes to transmit across a Linux raw socket on the specified interface."
    #Many network cards will require you turn off its settings that enable autocorrecting of packet checksums
    #os.system("ethtool -k lo tx off")
    #time.sleep(0.5)
    #Only going to work on linux raw sockets
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    raw_socket.bind((interface, 0))
    #Send pkt
    raw_socket.send(raw_bytes)
    #Clean up all that stuff we just did
    raw_socket.close()
    #os.system("ethtool -K lo tx on")


def hexdump_format(hex_bytes, length=16):
    "This method takes raw bytes and prints them in tcpdump hex format."
    lines = []
    for hexes in range(0, len(hex_bytes), length):
        chars = hex_bytes[hexes:hexes+length]
        hex = ' '.join([format(x, "02X")  for x in chars])
        text = ''.join([(chr(x) if chr(x) in string.ascii_letters+string.digits+string.punctuation else ".") for x in chars])
        lines.append("{hexes:04x}: {hex: <{width}} {text}".format(hexes=hexes,hex=hex, width = length*3, text=text) )
    return '\n'.join(lines)