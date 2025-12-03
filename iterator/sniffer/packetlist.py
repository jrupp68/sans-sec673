import socket
import os
import struct
import datetime
import pathlib

from sniffer.protocols import *
from sniffer.packet import Packet

#Define a new class called a PacketIterator() here
    #The init should accept a PacketList() as its only argument and do these things:
        #The init must use super() to get an instance of the PacketList object parent's iterator
        #The init needs to record the display_filter attribute from the PacketList in an attribute on self
    #You need a dunder next method that does all of the following:
        #It retrieves the next() value from the iterator recorded by init repeatedly to find the next packet that matches the display_filter recorded in init
        #If you reach the end of the list raise a StopIteration exception
class PacketIterator(object):

    def __init__(self, pktlist):
        self.iter =  super(PacketList,pktlist).__iter__()
        self.filter = pktlist.display_filter

    def __next__(self):
        val = next(self.iter)
        if self.filter != None:
            while val != self.filter:
                val = next(self.iter)
        return val


class PacketList(list):     
    def __init__(self, iterable=[]):
        if not isinstance(iterable, list):
            raise TypeError
        super().__init__()
        self.extend(iterable)
        self.no_ethernet =  os.name == "nt"
        self.capture_filter = None
        self.display_filter = None

    #This object needs a dunder iter method defined
        #It should return a new PacketIterator object
        #You need to pass a copy of self to the new PacketIterator
    def __iter__(self):
        return PacketIterator(self)

    #This object needs a new dunder len method defined
        #It should return a length that counts the number of items that match self.display_filter

    def __len__(self):
        return len([x for x in self])

    def __setitem__(self, pos, data):
        if not isinstance(data, Packet):
            raise TypeError
        super().__setitem__(pos, data)

    def extend(self, iterable):
        if not isinstance(iterable,list):
            raise TypeError
        for eachitem in iterable:
            self.append(eachitem)

    def insert(self, pos, data):
        if not isinstance(data, Packet):
            raise TypeError
        super().insert(pos, data)

    def append(self,data):
        if not isinstance(data, Packet):
            raise TypeError
        super().append(data)

    def rdpcap(self, filename):
        file_path = pathlib.Path(filename)
        if not file_path.is_file():
            raise ValueError("The specified pcap file does not exists.")
        with file_path.open("rb") as pcap_handle:
            #First 24 bytes are pcap file header info. I ignore most of it.
            file_header = pcap_handle.read(24)
            magic, *_ = struct.unpack("IHHIIII",file_header)
            assert magic in [0xa1b2c3d4, 0xa1b23c4d], "Unrecognized PCAP format"
            #Next 16 bytes are the pcap header for the first packet
            pkt_header = pcap_handle.read(16)
            while pkt_header:
                ts_s, ts_ms, plen, olen = struct.unpack('IIII', pkt_header )
                #Packet header says how much data is in the packet (plen)
                pkt_data = pcap_handle.read(plen)
                if not pkt_data:
                    break
                new_packet = Packet()
                new_packet.from_bytes(pkt_data)
                #These three lines are added from filter lab
                if self.capture_filter:
                    if not new_packet == self.capture_filter:
                        pkt_header = pcap_handle.read(16)
                        continue 
                new_packet.time = datetime.datetime.fromtimestamp(ts_s)
                self.append(new_packet)
                #Then there might be another packet pcap header
                pkt_header = pcap_handle.read(16)


    def sniff(self, count, prn = None, store=True):
        if self.no_ethernet:
            #Raw sockets on Windows
            localhost = socket.gethostbyname(socket.gethostname())
            raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW)
            raw_socket.bind((localhost, 0))
            raw_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            self.no_ethernet=True
        else:
            #Raw sockets on Linux
            raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        sniff_count = 0
        while sniff_count < count:
            data = raw_socket.recv(65535)
            new_packet = Packet()
            new_packet.from_bytes(data, self.no_ethernet)
            #These three lines are added from filter lab
            if self.capture_filter:
                if not new_packet == self.capture_filter:
                    continue 
            sniff_count += 1
            new_packet.time = datetime.datetime.now()
            if prn:
                print(prn(new_packet))
            if store:
                self.append(new_packet)
