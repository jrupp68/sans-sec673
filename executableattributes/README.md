# Lab - Executable Attributes

## Lab Objectives
In this lab, you will learn to create object attributes that are actually executable code.

## Instructions

Scapy allows you to extract the payload from a Protocol() with the .payload attribute. Each time you add .payload to the end of your object, you go down another layer. For example, in Scapy this works:

```
>>> pkt = Ether() / IP() / TCP() 
>>> pkt['IP'].payload
<TCP  |>
>>> pkt['Ether'].payload
<IP  frag=0 proto=tcp |<TCP  |>>
>>> pkt['Ether'].payload.payload
<TCP  |>
>>> pkt['IP'].payload
<TCP  |>

```

We want to improve on this functionality by allowing you to navigate UP to the encapsulating protocol or DOWN to the encapsulated protocol.

```
>>> from sniffer.protocols import *
>>> from sniffer.packet import Packet
>>> pkt = Packet([ Ether() , IP() , TCP()])
>>> pkt[0].encapsulated
IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> pkt[0].encapsulated.encapsulated
TCP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> pkt[0].encapsulated.encapsulated.encapsulator
IP(header=45454545454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> pkt[0].encapsulated.encapsulated.encapsulator.encapsulator
Ether(header=45454545454545, payload=b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
>>> pkt[0].encapsulator == None
True
```

Notice that we can move down a layer on a packet with `.encapsulated` or up a layer with `.encapsulator`. If either `.encapsulated` or `.encapsulator` have no additional protocols to step into, it should return None.

Add these two methods to your Protocol() class definition. This will also require that you make some minor changes to the Packet() class definition.

## Submit your answer

When you are finished, submit the entire `executableattributes` directory.

```
>>> d.solution("~/Desktop/executableattributes/")
```