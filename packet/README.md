# Lab - Packet

## Lab Objectives
In this lab, you will be starting the development of a Packet() object. You are only expected to modify 'packet.py'.

Your Packet object must satisfy all of the following requirements:
 - It must be a descendant of a UserList
 - Your modified UserList object must have a new `.append`, `.insert`, `.extend`, `.__setitem__` and `.__init__`
 - All of its input methods must verify that its inputs are of type `Protocol`
 - If any input is not of type `Protocol`, the method must raise a `TypeError`
 - Your Packet class must be implemented in the file called 'packet.py'
 - 'packet.py' must sit at the top level of the sniffer folder
 - Like the original list __init__ method your must optionally accept a list of values to assign to the object at creation

A unittest is provided for this lab. You are encouraged to use the Visual Studio Code integrated testing like we did in the `unittest` lab. Confirm that your new Packet class passes all of the tests in the provided unittest. If you would like to confirm it passes the test via the command line, you can type the following:

```
$ cd ~/Desktop/packet
$ python -m unittest
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## Full Walk Through

A full walk through is provided in the workbook.

### Submitting your Solution

When you have finished, you will submit 'packet.py'

```
>>> d.solution("~/Desktop/packet/sniffer/packet.py")
Correct! 
test_packet_append (test.TestSolution) ... ok
test_packet_extend (test.TestSolution) ... ok
test_packet_init (test.TestSolution) ... ok
test_packet_insert (test.TestSolution) ... ok
test_packet_setitem (test.TestSolution) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```