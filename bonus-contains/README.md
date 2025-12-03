# Lab - Bonus Contains

## Lab Objectives
In this lab you will add a "haslayer()" method to a Packet() object and associate that method with the keyword "in". 

## Instructions

### Define haslayer( 'PROTOCOL' )
The Packet() object must have a method named `.haslayer()`. It must accept a string as an argument and check to see if any of the Protocol() objects in that Packet() object have a name that matches the string.


```
>>> from sniffer.protocols import *
>>> from sniffer.packet import Packet
>>> pkt = Packet([ Ether(), IP() , ICMP()])
>>> pkt.haslayer("UDP")
False
>>> pkt.haslayer("TCP")
False
>>> pkt.haslayer("IP")
True
>>> pkt.haslayer("ICMP")
True
```

### Support Keyword 'in'

You must also be able to use the keyword "in" to call the .haslayer() method.

```
>>> "UDP" in pkt
False
>>> "ICMP" in pkt
True
```

## Submit your answer
When you are finished submit the single updated file called `packet.py` from the `sniffer` directory.

```
>>> d.solution("~/Desktop/bonus-contains/sniffer/packet.py")
```