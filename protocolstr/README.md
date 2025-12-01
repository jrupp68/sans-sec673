# Lab - Protocol Dunder str

## Lab Objectives
In this lab, you will be writing a `__str__` method for your protocols so that the sniffer will print some nice human readable output. Your goal is to write a dunder str method for as many protocols as you can in the time provided. The pyWars server will expect that you submit only `ethernet.py` to confirm it was done properly. 


## Instructions

Good news! We added a few more protocol parsers to your sniffer. It can now parse IP, UDP and ICMP packets!

In this lab, you will add a `__str__` method to Ether(), IP(), UDP and ICMP() objects so that they look nice when printed by the sniffer. At the moment, the sniffer just prints the output of the Protocol.repr() method. That means the sniffers output is not very easy to look at. If you are stretched for time, please note that the pyWars solution method will only ask you to submit one of the four updated protocols. Work on the `__str__` method for the Ether() protocol first.


Modify the required files in the `sniffer/protocols` folder. Test your code by running the sniffer, as shown here:

```
$ cd ~/Desktop/protocolstr
$ sudo -s PATH=$PATH python -m sniffer.sniff
```

Observe how the output is improved when the str() method is used instead of the default repr(). Using the str() method, you will transform the output from something that looks like this: (Data truncated to save space)

```
 Ether(header=ffffffffffff80, payload=b'\x00\x01\x08\x00\x06\x04\x00\x01\x80')
 Ether(header=ffffffffffff80, payload=b"E\x00\x00\xde\xea\x41\x00\x00\xff\x11")
-- IP(header=450000dea0340000ff11, payload=b"\xb8\x12\xa0\x0b\x00\xed\x99B\x00\")
---- UDP(header=c0021a0b, payload=b"\x00\x00U\xaa\x00\x00\x00\x00\x00\x00\x00")
```

To something like this:
```
 ff:ff:ff:ff:ff:ff > bc:dd:de:ad:be:ef Ethernet Type 2054
 ff:ff:ff:ff:ff:ff > bc:dd:be:ef:de:ad Ethernet Type 2048
-- 193.168.100.192 > 255.255.255.255 Protocol UDP
---- UDP Port 49154 > UDP Port 6667
```

### Walk-Through

A complete walkthrough for this lab is available in your course workbook.

## Submitting your Solution
After you have completed the required changes, submit `ethernet.py`
```
>>> d.solution("~/Desktop/protocolstr/sniffer/protocols/ethernet.py")
```
