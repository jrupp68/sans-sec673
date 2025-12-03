import ipaddress
import datetime

class IPRecord(object):
    def __init__(self,ip,name):
        if not isinstance(ip,str):
            raise TypeError
        self.address = ipaddress.ip_address(ip)
        self.__name = name

    def __repr__(self):
        return f"IPRecord('{str(self.address)}','{str(self.__name)}')"

    def __str__(self):
        return f"HOST: {self.__name} at address {str(self.address)}"
