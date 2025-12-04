# Lab - Context Manager

## Lab Objectives
In this lab, we will learn to implement context manager.

## Instructions

### Filter Classmethods
The Filter class will have a new Class Attribute, called `.combine_filters`, that will be a list.

You must add a new classmethod, named `.add_filter()`, which will accept a Filter object and add it to the `.combine_filters` list.

You must add a new classmethod, named `.del_filter()`, which will erase the filter in the last position in the `.combine_filters` list.

### The all_match Method
The filter class must implement a method named all_match(). It will take one argument. That argument will be a Packet() object. This method will return True if the packet passed in the argument matches both self and all of the filters in the `.combine_filters` list.

### The any_match Method
The filter class must implement a method named any_match(). It will take one argument. That argument will be a Packet() object. This method will return True if either self or any of the filters in the `.combine_filters` list match the specified Packet() object.

### The none_match Method
The filter class must implement a method named none_match(). It will take one argument. That argument will be a Packet() object. This method will return True if the Filter() in self and none of the Filter() objects in the `.combine_filters` list match the specified Packet() object. Otherwise, it will return False.

### Context Manager
The filter class must implement the methods needed to provide context managers. Calling dunder enter on the context manager will correspond to calling `.and_filter()`. When a context manager exits by calling dunder exit, it will simply remove the last item added to the `.combine_filters` list.

### Example Filter Interactions

Here is an example of using the Filter objects as context managers.

```
>>> from sniffer.filter import Filter
>>> from sniffer.protocols import *
>>> pkt = Ether() + IP() + TCP()
>>> pkt['IP'].ip_src = "1.1.1.1"
>>> pkt['TCP'].tcp_sport = 80
>>> with Filter("IP","ip_src","1.1.1.1"):
...     with Filter("TCP","tcp_sport",80) as filter_group:
...         print(filter_group.combine_filters)
...         print( filter_group.all_match(pkt))
...         print( filter_group.any_match(pkt))
...         print( filter_group.none_match(pkt))
... 
[Filter(protocol='IP', field='ip_src', value = ['1.1.1.1']), Filter(protocol='TCP', field='tcp_sport', value = 80)]
True
True
False
>>> Filter.combine_filters
[]

```

## Submit your answer
When you are finished, submit the single updated file called `filter.py` from the `sniffer` directory.

```
>>> d.solution("~/Desktop/context_manager/sniffer/filter.py")
```
