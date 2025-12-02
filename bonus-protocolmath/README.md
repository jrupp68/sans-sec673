# Lab - Bonus Protocol Math

## Lab Objectives
In this lab you will learn to add support for in-place math operators to your Packet() object.

## Instructions

In-place Math operators can be very helpful for saving memory when adding large data structures. After you have complete this update the following code should work.

```
>>> pkt = Ether() + IP()
>>> pkt += TCP()
```

Unlike `pkt = pkt + TCP()` this does not create a new Packet object but instead just updates the `pkt` object with the new Protocol() object. In other words you must add in in-place version of `__add__` to your Packet() object.

The method must confirm that the value being added is either a Protocol() or Packet() object. It should return NotImplemeted if it is not.

Your method must implement the in-place addition code locally and cannot rely on external methods or object to do the work.

## Submit your answer

When you are finished submit the updated `packet.py` file.

```
>>> d.solution("~/Desktop/bonus-protocolmath/sniffer/packet.py")
```