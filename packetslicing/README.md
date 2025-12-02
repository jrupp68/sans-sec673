# Lab - Packet Slicing

## Lab Objectives
In this lab, we will make our Packet() object behave more like Scapy by allowing you to slice out a Protocol() by its name. To complete this lab you will only need to make changes to `packet.py`.

After making the required changes to your Packet object, it should behave like this:

```
>>> from sniffer.packet import Packet
>>> from sniffer.protocols import *
>>> mypkt = Packet( [ Ether(), IP(), UDP(), ICMP() ] )
>>> mypkt[2]
UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> mypkt[::-1]
[ICMP(header=4545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> mypkt['Ether']
Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> mypkt['UDP']
UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> mypkt['doesntexist']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/student/Desktop/packetslicing/sniffer/packet.py", line 40, in __getitem__
    raise KeyError
KeyError
>>> mypkt[{}]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/student/Desktop/packetslicing/sniffer/packet.py", line 41, in __getitem__
    raise TypeError       
TypeError
```

If you slice a value out of a Packet() object with either an integer or the name of a protocol, it will return the Protocol at that position or with that name, if it exists in the Packet() object. 
If the integer or name does exist in the Packet() object, then it will raise a KeyError.
If the slice is neither an integer,a string or a slice, then it will raise a TypeError.
If the key is a slice object, then it will simply be passed on to the underlying .data data structure.

## Full Walk Through

A full walk through is provided in the workbook.

### Submitting your Solution

When you have finished, you will submit "packet.py"

```
d.solution("~/Desktop/packetslicing/sniffer/packet.py")