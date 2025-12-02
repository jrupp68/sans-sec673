# Serialization Attacks

## Overview

This lab contains a server that are vulnerable to serialization attacks. Exploit the servers with a deserialization attack that creates a file on the hard drive at the path "/tmp/you-got-owned". If you successfully exploit the vulnerability the server will respond back with the message "It appears that I've been owned."

### Attacking Vulnerable Server 1
First download the challenge to your machine by requesting the data.

```
>>> d.data("bonus-pickler")
'Zip extracted to /home/student/Desktop/bonus-pickler'
```

To obtain a copy of the vulnerable server and start it use the following commands in a new Terminal window.  These commands will use 7zip to extract the password protected binary from the ~/Documents/data folder to the folder on your Desktop. If you changed where you pywars writes files to you will need to adjust the commands accordingly. The binary must be in the same folder as the files provided by pyWars.

```
$ cd ~/Desktop/bonus-pickler/
$ 7z -pb7C4e1EG5lfBeSsu7QiO38mncZ78cefnPpo x ~/Documents/data/pickle-server1.zip
$ ./vulnerable_server.bin
Waiting on data to deserialize...

```

Now examine the contents of `serialize_me.py` in Visual Studio code or using `cat` at the CLI. Here is its contents.

```
$ cat ~/Desktop/bonus-pickler/serialize_me.py 
#This object is serialize by attacker.py and sent to vulnerable_server
class MyClass(object):
      myattr = "ECHO THIS"
```

This program just defines an object called MyClass that has a "myattr" attribute with a value of "ECHO THIS".  Now look at the attacker script `attacker.py`.

```
$ cat ~/Desktop/bonus-pickler/attacker.py 
import socket
import pickle
from serialize_me import MyClass

data = pickle.dumps(MyClass())

s = socket.socket()
s.connect(("127.0.0.1", 9000))
print("Sending data")
s.sendall(data)
print(s.recv(65535))
```

This program will create an instance of the MyClass() object we just looked at. Then it will use pickle to convert it into a byte string and send it to port 9000 on localhost. The vulnerable server is listening on that port. It then listens for the response from the vulnerable server and prints what it receives to the screen.   Lets run it.

```$ python attacker.py 
Sending data
b'The message was :ECHO THIS'
```

The attacker script serializes some data and sends it to the vulnerable_server. Then vulnerable_server deserializes the data and echoes back to you whatever is in the ".myattr" attribute of the object. The message we got back from the server was "ECHO THIS".

Now look back and the window where you ran the vulnerable_server. You should see this:

```
Waiting on data to deserialize...
data received 42
rm: cannot remove '/tmp/you-got-owned': No such file or directory
ECHO THIS
Waiting on data to deserialize...
```

On the server side we can see that it successfully deserialized the MyClass() object instance and printed the myattr value "ECHO THIS" that is set in `serialize_me.py`. Your job is to modify the MyClass object in the `serialize_me.py` program to cause the vulnerable server to execute code that will create a file call "/tmp/you-got-owned". If you successfully create that file the server will respond back with the message "It appears that I've been owned.".

### Submitting your answer.

After you have successfully exploited the vulnerable_server on your own machine submit `serialize_me.py` to the server.

``` python
>>> d.solution("~/Desktop/bonus-pickler/serialize_me.py")
Correct!
```