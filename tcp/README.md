# Lab - The TCP Protocol

## Lab Objectives
In this lab, you will be inherit a Protocol object and adopt it to be a TCP() object. 

## Instructions

Note: Each new lab retrieves a clean starting place that is independent of changes from previous labs. You are not required to use the new environment each time. If you want to accumulate the changes you just made in the previous lab, you may choose to work in the same folder as before and accumulate all your changes into a single project. This is not required or suggested, but it is permitted. 

This version sniffer is not printing the str() or the repr(). This version is printing the `.parsed` dictionary that is created for each protocol that is processed. When it runs, it should look something like this:

```
{'DST_MAC': b'84e3deadbeef', 'ETYPE': 2048, 'SRC_MAC': b'ffffffffffff'}
{'ip_byte0': 69,
 'ip_chksum': 9669,
 'ip_dst': '255.255.255.255',
 'ip_frag': 0,
 'ip_id': 35253,
 'ip_proto': 17,
 'ip_src': '192.168.100.170',
 'ip_svc': 0,
 'ip_total_len': 200,
 'ip_ttl': 255}
{'udp_chksum': 19005, 'udp_dport': 32414, 'udp_len': 29, 'udp_sport': 43407}
```

But this won't work until you complete the TCP Class parser. In this lab, you will create a new TCP Class inside of the file `sniffer/protocols/tcp.py`

Your TCP Class object must be a descendant of a Protocol and use the Protocol's dunder init to process the input bytes. You may want to look at the existing Ether() parser and use it as a model.

Your TCP Class object should use the following header values:

```
    header_format = '!HHIIBBHHH'
    header_length = 20
    header_fields = ["tcp_sport","tcp_dport","tcp_seq","tcp_ack","tcp_hlen","tcp_flag","tcp_window","tcp_chksum","tcp_urg"]
```

You must also add a process() method that matches the following specification:

 - It must accept one argument in addition to self, called "bytes_in". This value will be passed to it by the inherited `Protocol.__init__` method.
 - It must call `Protocol.process()` to process `bytes_in` using super().
 - Just like Ether() added a new 'SRC_MAC' key to the .parsed dictionary, you must add one called "tcp_flagstr" that contains a string representation of the "tcp_flag" field
 - It should rely on a new static method named `tcp_flag_as_str()` that converts the value in "tcp_flag" attribute to a string
 - It should also add a new key to the .parsed dictionary called "tcp_sportstr" that has a string representing the tcp_sport. It provides a string for port 80 ('http'), 443 ('https') and port 22 ('ssh')
 - It should add a new key to the .parsed dictionary called "tcp_dportstr" that has a string representing the tcp_dport. It provides a string for port 80 ('http'), 443 ('https') and port 22 ('ssh')

You must also add a `tcp_flag_as_str()` method to the TCP object that meets the following specification:

 - It must accept one and only one argument called "flags".  This will be an integer from TCP header.
 - It must return a string that represents the flags using the following strings: 'CWR',  'ECE', 'URG', 'ACK', 'PSH', 'RST', 'SYN', 'FIN' corresponding to each of the 8 bits. Each set will be joined together by a pipe "|". The name string should appear left to right in the same order they appear in the byte flags. Here are some example inputs and the expected output:

 ```
 >>> from sniffer.protocols import TCP
 >>> TCP.tcp_flags_as_str(2)
'SYN'
>>> TCP.tcp_flags_as_str(18)
'ACK|SYN'
>>> TCP.tcp_flags_as_str(16)
'ACK'
>>> TCP.tcp_flags_as_str(128+32)
'CWR|URG'
>>> TCP.tcp_flags_as_str(128+32+8)
'CWR|URG|PSH'
```

### Walk-Through

A complete walk through for this lab is available in your course workbook.

## Submitting your Solution
After you have completed the required changes, submit `tcp.py`
```
>>> d.solution("~/Desktop/tcp/sniffer/protocols/tcp.py")
```