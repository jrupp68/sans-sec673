# Lab - Saved Pickles

## Lab Objectives
In this lab, we will use a pickled object and save it to the disk and reload it. 

## Instructions

Our PacketList() object has no way of saving packets for later use. After you create a PacketList object filled with packets, you should be able to call `.save()` and store them externally. Then, when you want to reload them, you should be able to call `.load()` to pick up where you left off. Alternatively, you could call `.load_new()`, which will return a copy of the loaded object instead of just updating the current PacketList() object.

Each of these methods can take one optional argument that will be the name of the file to save or load. If no name is specified, it should use the file name "sniffer_state.bin".

The save method will just overwrite any file that already exists with the specified name.
The load and load_new will raise an exception if the file does not exist.

### Example Interaction with Object

```
>>> from sniffer.packetlist import PacketList
>>> from sniffer.protocols import *
>>> pkts = PacketList()
>>> pkts.append( Ether() + IP() + TCP() )
>>> pkts.append( Ether() + IP() + TCP() )
>>> pkts.append( Ether() + IP() + TCP() )
>>> len(pkts)
3
>>> pkts.save()
>>> del pkts[0]
>>> del pkts[0]
>>> del pkts[0]
>>> pkts
[]
>>> pkts = pkts.load_new()
>>> len(pkts)
3
>>> del pkts[0]
>>> del pkts[0]
>>> del pkts[0]
>>> pkts.load()
>>> len(pkts)
3
>>> pkts.load("doesntexist")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/student/Desktop/spf100/sniffer/packetlist.py", line 69, in load
    with pathlib.Path(fname).open("rb") as file_handle:
  File "/usr/lib/python3.10/pathlib.py", line 1117, in open
    return self._accessor.open(self, mode, buffering, encoding, errors,
FileNotFoundError: [Errno 2] No such file or directory: 'doesntexist'
```

## Submit your answer
When you are finished, submit the single updated file called `packetlist.py` from the `sniffer` directory.

```
>>> d.solution("~/Desktop/saved-pickles/sniffer/packetlist.py")
```