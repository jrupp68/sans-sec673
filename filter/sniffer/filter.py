from sniffer.protocols import *


class Filter(object):
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
        #complete this function as a static method
        #It has one input. A string that may be a single ip address or an address with a network CIDR mask
        # Check to see if a "/" is in the address stored in variable addr
            # If it is use ipaddress.ip_network() to turn it into a list of ip address objects
            # Passing strict=False to ipaddress.ip_network() means the address can be anywhere in the range, it doesnt have to be the first address in the range
            # Then turn each ipaddress object into a string
        # If address was just a single address (not a range with a mask), make it the only item in a list
        # return a list of strings that are ip addresses 


    def __eq__(self, other):
        #complete this dunder method
        #The other argument is a Packet() object you will compare to this filter. 
        #Return True if it matches the Filter (self) or False if it does not.
        #First confirm the other argument is not a Protocol object. if it is raise a TypeError
        #Next check to see if it is an instance of a list object (see Workbook for why we dont check for Packet)
            #Use a FOR loop to go through all of the Protocols in the "other" packet
                #Find the one that has a name that matches the .protocol attribute on this filter
                    #Get the value stored in the Protocol object specified in the filters.field
                    #You can use getattr() to retrieve a value from a specific field. Something like getattr(otherprotocol, self.field)
                    #The filters .value might be a list of possible values or a single value
                    #If it is a list confirm that the protocol is one of the value in that list. If so return True
                    #If it was a single value confirm that the protocol value matches the value. If so return True
                #If the values didn't match or the packet doesnt have the protocol return False
        #If other wasn't a list of protocols return NotImplemented 

    def __repr__(self):
        #complete this function
        #Your filter object should have repr that produces a string similar to the way you create a filter
        #Something like "Filter(protocol='{the protocol you filter on}', field='{the field to match}', value = {the expected value})"