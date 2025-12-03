import random

class Secure1(object):
    def __init__(self, value):
        self.admin=False
        self.__the_actual_variable = value
    @property
    def value(self):
        if not self.admin:
            return "Access Denied"
        return self.__the_actual_variable
    @value.setter  
    def value(self,val):
        self.__the_actual_variable = val
    @value.deleter 
    def value(self):
        del self.__the_actual_variable


class PrivateAttrib(object):
    def __init__(self, value=None):
        self.__value = value
    def __get__(self, obj, objtype):
        if not obj.admin:
            return "Access Denied"
        return self.__value
    def __set__(self, obj, value):
        if not obj.admin:
            raise(Exception("Read only!!"))
        self.__value = value

class Secure2(object):
    value = PrivateAttrib()
    def __init__(self,val):
        self.admin = True
        self.value = val
        self.admin = False


class Secure3(object):
    def __init__(self,value):
        super().__setattr__("admin",False)
        super().__setattr__("value",value)
    def __getattribute__(self,name):
        if not super().__getattribute__("admin"):
            return "Access Denied"
        else:
            return super().__getattribute__(name)
    def __setattr__(self, name, value):
        if name != "admin":
            print("You can not set any attributes.")
        else:
            super().__setattr__("admin",value)
        

secure1 = Secure1(random.randint(0,999999))
secure2 = Secure2(random.randint(0,999999))
secure3 = Secure3(random.randint(0,999999))