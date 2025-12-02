# Lab - Protocol Attributes

## Lab Objectives
In this lab, you will learn to overwrite the normal Python methods that are used to access object attributes.

## Instructions

Scapy allows you to access a Protocol() object's fields by treating them as attributes.

```
>>> IP().src
'127.0.0.1'
>>> TCP().dport
80
>>> UDP().sport
53
```

We currently have to do this:

```
>>> from sniffer.protocols import *
>>> IP().parsed['ip_src']
'69.69.69.69'
>>> TCP().parsed['tcp_dport']
17733
>>> UDP().parsed['udp_sport']
17733
```

Add dotted attribute access do your Protocol() object such that all of the values in the .parsed attribute can be read as object attributes.

If you attempt to read an attribute that is neither a normal object attribute nor a key in the .parsed dictionary, then you should raise an AttributeError.


```
$ cd ~/Desktop/protocolattributes
$ python
>>> from sniffer.protocols import *
>>> IP().ip_src
'69.69.69.69'
>>> TCP().tcp_dport
17733
>>> UDP().udp_sport
17733
>>> UDP().doesnt_exist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/student/Desktop/sec673_code/security_professionals_friend/sniffer/protocols/protocol.py", line 40, in __getattr__
    raise AttributeError(f"{self.name} has no attribute {name}")
AttributeError: UDP has no attribute doesnt_exist

```

## Submit your answer
When you are finished, submit the single updated file called `protocol.py` from the `protocols` directory.

```
>>> d.solution("~/Desktop/protocolattributes/sniffer/protocols/protocol.py")
```
