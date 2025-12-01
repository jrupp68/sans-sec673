# Circular Import 2

## Description

The sniffer module in our SPF100 tool kit has a circular reference in it. Find it and fix it!


## Overview

When you attempt to run the sniffer, it generates the following error:

```
$ python -m sniffer.sniff
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/student/Desktop/circularimport2/sniffer/sniff.py", line 2, in <module>
    import sniffer.protocols
  File "/home/student/Desktop/circularimport2/sniffer/protocols/__init__.py", line 2, in <module>
    from sniffer.protocols.ethernet import Ether
  File "/home/student/Desktop/circularimport2/sniffer/protocols/ethernet.py", line 4, in <module>
    class Ether(sniffer.protocols.protocol.Protocol):
AttributeError: module 'sniffer' has no attribute 'protocols'
```

To resolve this, you will ONLY be modifying one file. Modify the file `./sniffer/protocols/ethernet.py`.

When you do resolve this error, you will still get a permissions error if you do not run the sniffer as root. Remember that to run something in a Python virtual environment with sudo you use the following syntax:

```
$ sudo -s PATH=$PATH python -m sniffer.sniff
```


## Submitting the solution.

When you are finished, you will only submit the completed `ethernet.py`.

```
d.solution("~/Desktop/circularimport2/sniffer/protocols/ethernet.py")
Correct!
```



