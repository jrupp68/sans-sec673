# Lab - Protocol Math

## Lab Objectives
In this lab, you will learn to overwrite the normal function of the math operators with custom functions.

## Instructions

Scapy allows you to concatenate Protocols() with the division operator. For example, in Scapy this works:

```
>>> pkt = Ether() / IP() / TCP()
```

We want similar functionality, but we will use the addition operator to add together our Protocols().

```
>>> pkt = Ether() + IP() + TCP()
```

In addition, we want to be able to add together Packet() and Protocol() objects as follows:

```
>>> pkt = Packet([Ether()]) + Packet([IP()])
>>> pkt = Packet([Ether()]) + IP()
>>> pkt = Ether() + Packet([IP()])
```

All of these math operations should produce a new Packet() object that contains the values in the added Packet() object and/or the Protocol() objects. They should appear in the order they were added, from left to right.

You can test your code by reproducing the following functions.

```
$ cd ~/Desktop/protocolmath
$ python
>>> from sniffer.protocols import *
>>> Ether() + IP()
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> Ether() + IP() + TCP()
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), TCP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> pkt1 = Ether() + IP() + TCP()
>>> pkt2 = IP() + ICMP()
>>> pkt1 + pkt2
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), TCP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), ICMP(header=4545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> pkt1 + UDP()
[Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), TCP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
>>> UDP() + pkt1
[UDP(header=45454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'), TCP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')]
```

## Submit your answer

When you are finished, submit the entire `protocolmath` directory.

```
>>> d.solution("~/Desktop/protocolmath/")
```