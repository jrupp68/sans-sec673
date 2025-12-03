# Lab - Filter

## Lab Objectives
In this lab, you will create a new type of object called a Filter(). This filter object must be implemented in the file "sniffer/filter.py". The filter object will be compared to a Packet() object and will return True if the Packet() object matches the values defined in the filter.

## Instructions

### New Changes in your Project

If you are accumulating changes into a separate project, you should be aware of the following file changes. The new file `packetlist.py` can be used to create a PacketList() object, as discussed in class. The file `packet.py` has been updated to include a new method called `from_bytes()` which will generate a Packet() object from a byte stream. It is used by `PacketList().rdpcap()` and `PacketList().sniff()`.

Also, `protocol.py` in this folder also has two additional methods defined for you. These are answers to two previous labs that we will establish as dependencies moving forward. Since you may not have finished those labs, I will give you working copies of these methods. Specifically, you will find `__add__` and `__getattr__` have been added to `protocol.py`.

### `Filter.__init__():`
Your Filter object will accept three values in its init. A Protocol, a field and a value. It will assign those values to object attributes named ".protocol", ".field" and ".value", respectively. The protocol and field arguments must be strings, but the value can be of any type.
If the protocol is "IP" and the field is either "ip_src" or "ip_dst", then the value will be checked to see if it contains a CIDR Network Mask. If it does, it will be expanded to match all of the IP Addresses in the specified network. 

### `Filter.__eq__():`
The filter object must contain a dunder eq method that will evaluate a packet to determine if it matches the specified filter. It should implement type checking and confirm that the other object is a Packet(). If the other object is a Protocol() it should raise a TypeError. If it is a Packet, it should return True or False, indicating whether or not the Packet() object matches the filter. For any other type, it should return NotImplemented.

### `Filter.__repr__():`
Your Filter() object should have a dunder repr method that will print a string that could be used to create the Filter object.
For example:
```
>>> x = Filter("TCP","tcp_dport",443)
>>> x
Filter(protocol='TCP', field='tcp_dport', value = 443)
```


### Some Sample Test Cases

You may use the following examples to test your code and confirm it is working properly.

```
>>> from sniffer.protocols import *
>>> from sniffer.filter import Filter
>>> pkt = Ether() + IP() + TCP()
>>> pkt['IP'].ip_src = "8.8.8.8"
>>> pkt['TCP'].tcp_dport = 443
>>> pkt == Filter("IP","ip_src","8.8.8.8")
True
>>> pkt == Filter("IP","ip_src","8.8.8.7")
False
>>> pkt == Filter("IP","ip_src","8.8.8.7/28")
True
>>> pkt == Filter("IP","ip_src","8.8.8.7/29")
False
>>> pkt == Filter("TCP","tcp_dport","443")
False
>>> pkt == Filter("TCP","tcp_dport",443)
True
>>> Filter("TCP","tcp_dport",443) == pkt
True
>>> Filter("TCP","tcp_dport",443) != pkt
False
>>> Filter("TCP","tcp_dport",443).__eq__(1)
NotImplemented

```


### Confirm .capture_filter works
Once you have confirmed your filter option works, then confirm it is operating when used as a .capture_filter.

The following capture filter should only capture IP Packets.

```
$ sudo -s PATH=$PATH python
>>> from sniffer.packetlist import PacketList
>>> pktlist = PacketList()
>>> pktlist.capture_filter = Filter("TCP","tcp_dport", 443))
>>> pktlist.sniff(10, prn=repr, store=False)
```

No packets should be displayed until you generate some web traffic to a secure website. When you do, confirm each of the captured packets is going to port 443.

Then, set the capture filter to None and compare the results. You should see significantly more traffic, including packets with no TCP protocol.

```
>>> pktlist.capture_filter = None
>>> pktlist.sniff(10, prn=repr, store=False)
```

## Submit your answer
When you are finished, submit the single updated file called `filter.py` from the `sniffer` directory.

```
>>> d.solution("~/Desktop/filter/sniffer/filter.py")
```