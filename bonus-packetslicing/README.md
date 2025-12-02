# Lab - Bonus Lab Packet Slicing

## Lab Objectives
In this lab you will make `__getitem__` on your Packet() object even more useful.


## Instructions

Currently a slicing operation with a `[start:stop:step]` on a Packet() object can only contain integers. Something like this works fine:

```
>>> mypkt = Packet( [ Ether(), IP(), UDP(), ICMP() ] )
>>> mypkt[1:3]
[IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
```

But this does not:

```
>>> mypkt['Ether': -1 ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/student/Desktop/sec673_code/security_professionals_friend/sniffer/packet.py", line 24, in __getitem__
    raise KeyError
KeyError
```

You must remedy this problem.  Slicing should support strings, integers or a combination of the two.

If a string is provided and it does not match a valid layer name then a KeyError should be raised.

Your Packet() object must also still pass all of the requirements of the `packetslicing` lab.

Here are some example iteractions that should work on your new object.
```
>>> from sniffer.protocols import *
>>> from sniffer.packet import Packet
>>> pkt = Packet([ Ether(), IP(), UDP(), ICMP() ] )
>>> pkt['Ether':'UDP']
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> pkt['Ether':]
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), ICMP(header=4545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> pkt[:'TCP']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/student/Desktop/bonus-packetslicing/sniffer/packet.py", line 51, in __getitem__
    stop = self.key2num(key.stop)
  File "/home/student/Desktop/bonus-packetslicing/sniffer/packet.py", line 39, in key2num
    raise KeyError
KeyError
>>> pkt[:'UDP']
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> pkt['Ether'::2]
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]

```



## Submitting your solution

When finished only submit your updated `packet.py`.

```
>>> d.solution("~/Desktop/bonus-packetslicing/sniffer/packet.py")
```