import socket
import os
import struct
import datetime
import pathlib
import zoneinfo

from sniffer.protocols import *
from sniffer.packet import Packet


class PacketList(list):     
    def __init__(self, iterable=[]):
        if not isinstance(iterable, list):
            raise TypeError
        super().__init__()
        self.extend(iterable)
        self.no_ethernet =  os.name == "nt"
        self.capture_filter = None
        self.display_filter = None

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

    @staticmethod
    def adjust_time(timestamp, from_zone, to_zone=None):
        #Raise TypeError if timestamp isnt a datetime.datetime
        if not isinstance(timestamp, datetime.datetime):
            raise TypeError("First arg must be a timestamp")
        #Raise TypeError if fromzone isn't in zoneinfo.available_timezones()
        if not from_zone in zoneinfo.available_timezones():
            raise TypeError("Second arg must be a valid timezone")
        #Get a tzinfo record from zoneinfo.ZoneInfo for the from_zone
        from_zone = zoneinfo.ZoneInfo(from_zone)
        #Convert timestamp to a timezone aware datetime in the from_zone timezone
        timestamp = timestamp.replace(tzinfo=from_zone)
        #If to_zone is None convert it to the local computer timezone
        if to_zone != None:
            if not to_zone in zoneinfo.available_timezones():
                raise TypeError('Third arg must be a valid timezone')
            to_zone = zoneinfo.ZoneInfo(to_zone)
        return timestamp.astimezone(to_zone)
        #If to_zone is not in zoneinfo.available_timezones() raise a TypeError
        #Get a tzinfo record from zoneinfo.ZoneInfo for the to_zone
        #Convert timestamp to the to_zone timezone
        #Return the new timezone

    def print_timezones(self, client, server):
        if not server in zoneinfo.available_timezones():
            raise TypeError("You must specify a valid timezone string.")
        if not client in zoneinfo.available_timezones():
            raise TypeError("You must specify a valid timezone string.")
        for eachpkt in self:
            pkt_time = eachpkt.time.replace(tzinfo=datetime.timezone.utc)
            server_time = self.adjust_time(eachpkt.time, "UTC", server)
            client_time = self.adjust_time(eachpkt.time, "UTC", client)
            local_time = self.adjust_time(eachpkt.time, "UTC", None)
            print(f"--- UTC {pkt_time} --- CLIENT {client_time} --- SERVER {server_time} --- LOCAL {local_time} ---")
            print(str(eachpkt))

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
