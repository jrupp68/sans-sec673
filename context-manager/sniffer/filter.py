import ipaddress

from sniffer.packet import Packet
from sniffer.protocols import *


class Filter(object):
    #Add a list or deque as a class attribute to store each instance of a filter that is created. 

    def __init__(self, protocol, field, value):
        if not isinstance(protocol, str):
            raise TypeError("The protocol must be a string")
        if not isinstance(field, str):
            raise TypeError("The field must be a string")
        if protocol == "IP":
            if field in ["ip_src","ip_dst"]:
                value = self.addr_to_list(value)            
        self.protocol = protocol
        self.field = field
        self.value = value

    @staticmethod
    def addr_to_list( addr ):
        if "/" in addr:
            return list(map(str, ipaddress.ip_network( addr , strict=False)))
        else:
            return [ addr ]

    def __eq__(self, other):
        if isinstance(other, Protocol):
            raise TypeError("Filters are compared to Packets not Protocols.")
        if isinstance(other,list):
            for eachlayer in other:
                if eachlayer.name == self.protocol:
                    layer = eachlayer
                    break
            else:
                return False
            myval = getattr( layer, self.field, "NOT FOUND")
            if myval == "NOT FOUND":
                return False
            if isinstance(self.value, list):
                return myval in self.value
            return myval == self.value
        return NotImplemented

    def __repr__(self):
        return f"Filter(protocol='{self.protocol}', field='{self.field}', value = {self.value})"

    #Add a new class method called add_filter that takes one argument
    #The argument will be the filter instance you are adding
    #This method should append a filter instance to the the class attribute storing all of the instances
    #That class attribute should be added at the top of this class definition
    
    #Add a new class method called del_filter that takes no arguments
    #This method should delete the last filter instance from the the class attribute storing all of the instances
    
    #Add the dunder that is called when a context manager is started
    #It should call add_filter and add the current object (self)
    #This dunder should always return self

    #Add the dunder that is called when a context manager code block is finished
    #This method should call del_filter

    #Add a method called all_match
    #It takes one argument which will be a Packet() object to check
    #Only return true when all filters in our combined filters class attribute match
    #You need a loop going through all of the filters stored in the class atribute
    #If any one of those doesn't match you can return False
    #If you go through the entire list and none of them returned False you can return True

    #Add a method called any_match
    #It takes one argument which will be a Packet() object to check
    #If any of the filters in our combined filters class attribute match it returns true
    #You will need a loop to go through our combined filters
    #If the current filter in the loop matches return True
    #If you go through the entire list and none of them returned True you can return False

    #Add a method called none_match
    #It takes one argument which will be a Packet() object to check
    #In order to not repeat functionality you can just negate any_match
    
