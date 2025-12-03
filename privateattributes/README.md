# Private Attribute Security

This folder contains two programs.

solution.py - This is the program you must complete
private_attributes.py - This program is imported by solutions.py

Solution.py will contain 3 objects named "secure1", "secure2" and "secure3".

Each of these objects have an attribute named "value" that you must retrieve. But the developer has attempted to prevent anyone from accessing the values through various means of obfuscation. Access to the value is protected by the "admin" attribute. Each object behaves as follows:

```
$ cd ~/Desktop/privateattributes
$ python 
>>> from private_attributes import *
>>> s3 = Secure3("Retrieve Me!")
>>> s3.value
'Access Denied'
>>> s3.admin=True
>>> s3.value
'Retrieve Me!'
>>> s3.admin = False
>>> s3.value
'Access Denied'
```

If .admin is set to True, then the value can be retrieved. If not, access is denied. Normally, rather than just being True or False, the .admin authenticates the user and checks their permissions to determine if they should have access, but we have simplified it here.

You must modify `solution.py` and rewrite the three functions named `secure1_value`, `secure2_value` and `secure3_value`. Your functions must successfully bypass the security and retrieve the value while the admin attribute is set to False.  When your code is tested by the pyWars server, changing the .admin attribute on the object will have no effect, because slightly different objects will be used. Other than having the admin always set to False, the object used during testing will behave identically to the one you are given. Your function must bypass the poorly written security and return the value.  

You should not make any modifications to `private_attributes.py`. Looking at the code inside `private_attributes.py` to see what the developer has tried to do to prevent you from accessing the values is a good first step.

To test your code, you can create objects like Secure1, Secure2 and Secure3, as shown below. Then, pass it to your secure1_value() function which successfully bypasses the protection and returns the value. 

```
>>> from private_attributes import Secure1
>>> x = Secure1("RETRIEVE THIS VALUE")
>>> x.admin = False
>>> secure1_value(x)
'RETRIEVE THIS VALUE'
```

When you have rewritten all three of these functions, submit the entire "privateattributes" folder using .solution().

```
>>> d.solution("~/Desktop/privateattributes/")
```

