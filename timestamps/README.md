# Lab - Timestamps

## Lab Objectives
In this lab, you will process the timestamps on Packet() object to show them in three different time zones. 

## Instructions
Every Packet() object has a .time attribute that records the creation of the record. If you create a Packet() object, it has the time you created it. If you sniff a Packet(), then it will have the time it was captured. 

Read the provided `ncat.pcap` or another pcap of your choosing using `.rdpcap()`. 

```
$ python
>>> from sniffer.packetlist import PacketList
>>> pkts = PacketList()
>>> pkts.rdpcap("ncat.pcap")
>>> pkts[0].time
datetime.datetime(2015, 12, 30, 15, 23, 47)
```

That time stamp is when the packet was captured by the sniffer in UTC. The actual time for the attacker transmitting the packet and the server capturing them are different (assuming neither are physically located in the UTC time zone). Our analysis requires that we determine if the attacks were launched during the attacker's normal business hours or if they adjusted their work schedule to avoid hours when the defenders were at work.  

There are three timezones of interest when looking at a Packet capture. The timezone of the client (attacker), the server and the analyst. You must write a new method for a `PacketList` object, called `adjust_time`. A function called `print_timezones()` that has been written for you will call the `adjust_time()` method that you are writing. It will print the packet's original UTC time and the three other time zones we are interested in.

At the moment all four timezones that are printed are exactly the same.

```
>>> pkts.print_timezones("US/Pacific","Australia/NSW")
--- UTC 2015-12-30 15:23:47+00:00 --- CLIENT 2015-12-30 15:23:47 --- SERVER 2015-12-30 15:23:47 --- LOCAL 2015-12-30 15:23:47 ---
Ether 00:00:00:00:00:00 > 00:00:00:00:00:00 Ethernet Type 2048
 + IP    127.0.0.1 > 127.0.0.1 Protocol TCP
 +  + TCP   SPORT: 52253 DPORT 9898 Flags 2
0000: 02 04 FF D7 04 02 08 0A 02 D2 FF F5 00 00 00 00  ................
0010: 01 03 03 07  
```

After you have completed the `adjust_time()` method as described here it will print four different time stamps.

### Write supporting function `PacketList().adjust_time(timestamp, from_zone, to_zone=None )`
Your PacketList object must have a static method that takes two or three arguments. The first argument is a timestamp that you want to adjust. The second argument is the timezone for the timestamp in the first argument. The third argument is the timezone it should be adjusted to, but this argument is optional. If the the third argument is not specified, then the timestamp in the first argument must be changed from the timezone in the second argument to the timezone on which the Python script is running (aka the analyst time). If a third argument is provided, then you will adjust the timestamp in the first position from the timezone in the second argument to the timezone in the third argument.

You must raise a TypeError if the first argument is not a datetime.datetime() object. 
You must raise a TypeError if the second argument is not in the list of `zoneinfo.available_timezones()`.
You must raise a TypeError if the third argument is not None, and it is not in the list of valid timezones listed in `zoneinfo.available_timezones()`.


### Example Interaction

Here is an example that would assume the PCAP was captured on a SERVER running in the "Australia/NSW" (+11) timezone. It shows the timestamp for a CLIENT that is in the "US/Pacific" (-8) timezone and it automatically determines that the analysts machine is in the "US/Eastern" (-5) timezone. 

Note: This is a sample of some of the packets you may see. Your packet output may look different, depending upon the challenges you have finished. The packet output is ignored by the pyWars server when evaluating the results.


```
>>> from sniffer.packetlist import PacketList
>>> pkts = PacketList()
>>> pkts.rdpcap("ncat.pcap")
>>> pkts.print_timezones("US/Pacific","Australia/NSW")
--- UTC 2015-12-30 15:23:47+00:00 --- CLIENT 2015-12-30 07:23:47-08:00 --- SERVER 2015-12-31 02:23:47+11:00 --- LOCAL 2015-12-30 10:23:47-05:00 ---
Ether 00:00:00:00:00:00 > 00:00:00:00:00:00 Ethernet Type 2048
 + IP    127.0.0.1 > 127.0.0.1 Protocol TCP
 +  + TCP   SPORT: 52253 DPORT 9898 Flags 2
0000: 02 04 FF D7 04 02 08 0A 02 D2 FF F5 00 00 00 00  ................
0010: 01 03 03 07                                      ....
--- UTC 2015-12-30 15:23:47+00:00 --- CLIENT 2015-12-30 07:23:47-08:00 --- SERVER 2015-12-31 02:23:47+11:00 --- LOCAL 2015-12-30 10:23:47-05:00 ---
Ether 00:00:00:00:00:00 > 00:00:00:00:00:00 Ethernet Type 2048
 + IP    127.0.0.1 > 127.0.0.1 Protocol TCP
 +  + TCP   SPORT: 9898 DPORT 52253 Flags 18
0000: 02 04 FF D7 04 02 08 0A 02 D2 FF F6 02 D2 FF F5  ................
0010: 01 03 03 07                                      ....
--- UTC 2015-12-30 15:23:47+00:00 --- CLIENT 2015-12-30 07:23:47-08:00 --- SERVER 2015-12-31 02:23:47+11:00 --- LOCAL 2015-12-30 10:23:47-05:00 ---
Ether 00:00:00:00:00:00 > 00:00:00:00:00:00 Ethernet Type 2048
 + IP    127.0.0.1 > 127.0.0.1 Protocol TCP
 +  + TCP   SPORT: 52253 DPORT 9898 Flags 16
0000: 01 01 08 0A 02 D2 FF F6 02 D2 FF F6              ............
--- UTC 2015-12-30 15:23:50+00:00 --- CLIENT 2015-12-30 07:23:50-08:00 --- SERVER 2015-12-31 02:23:50+11:00 --- LOCAL 2015-12-30 10:23:50-05:00 ---
Ether 00:00:00:00:00:00 > 00:00:00:00:00:00 Ethernet Type 2048
 + IP    127.0.0.1 > 127.0.0.1 Protocol TCP
 +  + TCP   SPORT: 52253 DPORT 9898 Flags 24
0000: 01 01 08 0A 02 D3 02 6C 02 D2 FF F6 48 65 6C 6C  .......l....Hell
0010: 6F 0A                                            o.

```

## Submit your answer
When you are finished, submit the single updated file called `packetlist.py` from the `sniffer` directory.

```
>>> d.solution("~/Desktop/timestamps/sniffer/packetlist.py")
```