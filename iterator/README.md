# Lab - Iterator

## Lab Objectives
In this lab, you will customize the way you step through a PacketList() object.

## Instructions

### New Changes to your Project

#### You've been given a functioning filter.py
I will give you a minimally functional Filter() object inside `filter.py`. If you didn't finish the filter lab earlier, then this one has the minimum requirements required for this lab. If your version had more functionality, feel free to replace the version that is provided with your own. But your version must satisfy the minimal requirements of the test, as shown here.

#### You've been given a "utils" module
Another new file has been added to your project. The file `sniffer/utils.py` contains some support functions that may be useful. The function `hexdump_format()` will take bytes and produce a string that mimics the output from tcpdump, xxd and other hex dump output utilities. It takes bytes and returns a string in the format we typically see with tcpdump. You can then print that string in addition to your protocol data.  

```
>>> from sniffer.utils import hexdump_format
>>> print(hexdump_format(b"print these hex bytes \xde\xad\xbe\xef"))
0000: 70 72 69 6E 74 20 74 68 65 73 65 20 68 65 78 20  print.these.hex.
0010: 62 79 74 65 73 20 DE AD BE EF                    bytes.....
```

A second function call `linux_send()` takes bytes and transmits them across the specified interface using raw sockets. The `linux_send()` function will only work on Linux.

#### You've been given some nice dunder str methods
Additionally, a `__str__` method was added to `ethernet.py`, `icmp.py`, `ip.py`, `tcp.py`, `udp.py` and `packet.py` so that the output from your sniffer will look like tcpdump.

### Make iteration use .display_filter

At the moment, a for loop will step through every packet in the PacketList. In this lab, you must modify the PacketList() object such that a for loop will only step through the packets that match the .display_filter attribute. That means building an iterator object.

### PacketIterator

You will create a new type of object called PacketIterator(). This object will have two methods. It will have a dunder init method that sets the starting position of the iterator at position zero. It will have a dunder next method that will retrieve the next Packet() in the PacketList() that matches the ".display_filter". When the end of the PacketList() is reached, it will raise a StopIteration exception.


### Example Iteraction
Here is an example of interacting with the PacketList() after you have added these changes.

```
$ python
>>> from sniffer.packetlist import PacketList
>>> from sniffer.filter import Filter
>>> pkts = PacketList()
>>> pkts.rdpcap("/home/student/Documents/data/web.pcap")
>>> pkts.display_filter = Filter("IP","ip_dst", "10.1.1.140")
>>> for pkt in pkts:
...     print(pkt)
... 

```

After setting the display filter, the for loop will only show you packets that match the display filter. 

```
Ether 00:0c:29:25:6c:15 > 00:0d:b9:27:07:80 Ethernet Type 2048
 + IP    212.58.244.91 > 10.1.1.140 Protocol TCP
 +  + TCP   SPORT: 80 DPORT 46792 Flags 24
0000: 01 01 08 0A 9E 83 05 BB 01 A2 A1 0B 48 54 54 50  ............HTTP
0010: 2F 31 2E 31 20 32 30 30 20 4F 4B 0D 0A 44 61 74  /1.1.200.OK..Dat
```

Notice that only Packet() objects that match the ".display_filter" are printed.

### Fix the length function
The inherited len() function does not iterate over the list. Therefore, it gives the total length of the PacketList and not the displayed packet length. Look at this example:

```
$ python
>>> from sniffer.packetlist import PacketList
>>> from sniffer.filter import Filter
>>> pkts = PacketList()
>>> pkts.rdpcap("/home/student/Documents/data/web.pcap")
>>> pkts.display_filter = Filter("IP","ip_src", "10.1.1.140")
>>> len(pkts)
1118
>>> pkts.display_filter = Filter("IP","ip_dst", "10.1.1.140")
>>> len(pkts)
982
>>> pkts.display_filter = None
>>> len(pkts)
2100
```

We want it to show us the number of packets we would see if we step through it with a for loop. The problem is that the `len()` function doesn't account for the `.display_filter`. 

Fix the len() function so that it only provides the number of packets that match the display filter.

## Submit your answer
When you are finished, submit the entire `iterator` directory.
```
>>> d.solution("~/Desktop/iterator/")
```