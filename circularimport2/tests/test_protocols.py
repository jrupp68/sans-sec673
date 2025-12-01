import unittest
import sniffer.protocols


class TestSolution(unittest.TestCase):

    def test_ether(self):
        p1 = sniffer.protocols.Ether(b"\x00"*14)
        print(p1.parsed)
        repr(p1)

    def test_ip(self):
        p1 = sniffer.protocols.IP(b"\x00"*20)
        print(p1.parsed)
        repr(p1)

    def test_tcp(self):
        p1 = sniffer.protocols.TCP(b"\x00"*20)
        print(p1.parsed)
        repr(p1)