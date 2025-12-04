In this lab you must create a new object called "IPRecord" with specific attributes and values. You must use the @dataclass decorator when creating your object. The provided solution.py will implement a few simple use cases when executed. You can manually confirm the proper functionality of your object using the example use cases below.


### Create IPRecord with the following attributes.
 - .address which has a default value of "127.0.0.1" and does not appear in the repr() of the object
 - .name which is a string. It has no defaults and does appear in the repr of the object.

It must also be created using the @dataclass decorator.

### Here is an example of using your object:
```
>>> rec_x = IPRecord("server")
>>> rec_x.address
127.0.0.1
>>> rec_x
IPRecord(name="server")
>>> rec_x.name
server
```



