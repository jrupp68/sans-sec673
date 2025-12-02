import unittest
from sniffer.protocols import *
from sniffer.packet import Packet

class TestSolution(unittest.TestCase):

    def test_packet_append(self):
        a_packet = Packet()
        self.assertRaises(TypeError, a_packet.append, 1)
        self.assertRaises(TypeError, a_packet.append, "str")
        self.assertRaises(TypeError, a_packet.append, [1,2])
        protocol1 = Ether()
        a_packet.append(protocol1)
        self.assertEqual(a_packet[0],protocol1,"Protocol.append does not appear to be working.")
        protocol2 = IP()
        a_packet.append(protocol2)
        self.assertEqual(a_packet[0],protocol1,"Protocol.append does not appear to be working.")
        self.assertEqual(a_packet[1],protocol2,"Protocol.append does not appear to be working.")
        

    def test_packet_insert(self):
        a_packet = Packet()
        self.assertRaises(TypeError, a_packet.insert, 0,1)
        self.assertRaises(TypeError, a_packet.insert, 0,"str")
        self.assertRaises(TypeError, a_packet.insert, 0, [1,2])
        protocol1 = Ether()
        a_packet.insert(0,protocol1)
        self.assertEqual(a_packet[0],protocol1,"Protocol.insert does not appear to be working.")
        protocol2 = IP()
        a_packet.insert(0, protocol2)
        self.assertEqual(a_packet[1],protocol1,"Protocol.insert does not appear to be working.")
        self.assertEqual(a_packet[0],protocol2,"Protocol.insert does not appear to be working.")
        protocol3 = Ether(b"\xff"*20)
        a_packet.insert(-1, protocol3)
        self.assertEqual(a_packet[2], protocol1,"Insert did not create the expected packet list.")
        self.assertEqual(a_packet[1], protocol3,"Insert did not create the expected packet list.")
        self.assertEqual(a_packet[0], protocol2,"Insert did not create the expected packet list.")

    def test_packet_init(self):
        a_packet = Packet()
        self.assertRaises(TypeError, Packet, [1,2,3])
        self.assertRaises(TypeError, Packet, 1)
        self.assertRaises(TypeError, Packet, [Ether(),IP(),5])
        protocol1 = Ether()
        protocol2 = IP()
        protocol3 = Ether(b"\xff"*20)
        a_packet = Packet([protocol1, protocol2, protocol3])
        self.assertEqual(a_packet[1], protocol2,"Init did not create the expected packet list.")
        self.assertEqual(a_packet[2], protocol3,"Init did not create the expected packet list.")
        self.assertEqual(a_packet[0], protocol1,"Init did not create the expected packet list.")
        a_packet = Packet([protocol2, protocol3, protocol1])
        self.assertEqual(a_packet[0], protocol2,"Init did not create the expected packet list.")
        self.assertEqual(a_packet[1], protocol3,"Init did not create the expected packet list.")
        self.assertEqual(a_packet[2], protocol1,"Init did not create the expected packet list.")

    def test_packet_extend(self):
        a_packet = Packet()
        self.assertRaises(TypeError, a_packet.extend, [1,2,3])
        self.assertRaises(TypeError, a_packet.extend, 1)
        self.assertRaises(TypeError, a_packet.extend, "str")
        self.assertRaises(TypeError, a_packet.extend, [Ether(),TCP(),5])
        protocol1 = Ether()
        protocol2 = IP()
        protocol3 = Ether(b"\xff"*20)
        a_packet = Packet([protocol1, protocol2, protocol3])
        b_packet = Packet([protocol3,protocol2])
        a_packet.extend(b_packet)
        self.assertEqual(a_packet[0], protocol1,"Packet.extend did not create the expected packet list.")
        self.assertEqual(a_packet[1], protocol2,"Packet.extend did not create the expected packet list.")
        self.assertEqual(a_packet[2], protocol3,"Packet.extend did not create the expected packet list.")
        self.assertEqual(a_packet[3:], b_packet,"Packet.extend did not create the expected packet list.")

    def test_packet_setitem(self):
        protocol1 = Ether()
        protocol2 = IP()
        protocol3 = Ether(b"\xff"*20)
        a_packet = Packet([protocol1, protocol2, protocol3])
        a_packet[0] = protocol3
        a_packet[2] = protocol1
        try:
            a_packet[1] = 5
            a_packet[1] = "test"
            a_packet[1] = []
        except TypeError:
            pass
        else:
            self.fail("Packet.__setitem__ should only accept Protocol objects.")
        self.assertEqual(a_packet[2], protocol1,"Packet.__setitem__ did not create the expected packet list.")
        self.assertEqual(a_packet[0], protocol3,"Packet.__setitem__ did not create the expected packet list.")

    def test_packet_getitem(self):
        protocol1 = Ether()
        protocol2 = IP()
        protocol3 = TCP()
        a_packet = Packet([protocol1, protocol2, protocol3])
        self.assertRaises(TypeError, a_packet.__getitem__, 3.1415)
        self.assertRaises(KeyError, a_packet.__getitem__, 'BogusLayerName')        
        self.assertEqual(a_packet[1], protocol2,"Packet.__getitem__ did not retrieve the expected value.")
        self.assertEqual(a_packet['IP'], protocol2,"Packet.__getitem__ did not retrieve the expected value.")
        self.assertEqual(len(a_packet[-2:]), 2 ,"Packet.__getitem__ doesn't support slicing values.")

if __name__ == "__main__":
    unittest.main()