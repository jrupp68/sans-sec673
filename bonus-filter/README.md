# Lab - Bonus Filter

## Lab Objectives
In this lab you will add flexibility to our Filter object by making the protocol field and value optional.

## Instructions

### Make Filter Protocol Fields Optional

To complete this bonus lab you should begin with a copy of the Filter object you wrote in the previous labs. Then you add an enhancement to make the Filter() object more user friendly. We may want to have Filter() object that only look for the presence of a specific protocol. Modify your Filter() object so that you can create a filter that only looks for the presence of a Protocol. This behaves similarly to the scapy "haslayer()" function and checks for the presence of a Protocol in a Packet.

### Example Object Interaction

Here are some interactions that your enhanced Filter() should provide.

```
>>> from sniffer.protocols import *
>>> from sniffer.packet import Packet
>>> from sniffer.filter import Filter
>>> pkt = Packet([ Ether(), IP(), TCP() ])
>>> pkt == Filter("IP")
True
>>> pkt == Filter("UDP")
False
```

## Submit your answer
When you are finished submit the single updated file called `filter.py` from the `sniffer` directory.

```
>>> d.solution("~/Desktop/bonus-filter/sniffer/filter.py")
```