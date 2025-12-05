# Logger Config Lab

In this lab you will create a configuration file for your loggers.

## Write a log configuration file

In this lab you will are required to generate the exact same logs that you generated in the "LoggingProblems" lab. The challenge here is that you can not alter any of the python programs. Instead you will only provide a file named "log.config". Your log.config file will be placed into the same directory as "calculator.py" and it will be read.  

The solution folder has a copy of the python programs that will use the logging config for your testing. You should not modify any of the python programs. The only file you should modify is "log.config".  Then only upload that file.

Of course you should configure this and run it on your own computer to get this working first. Then upload "log.config" using solution.  Here is what the output of your program should look like.

```
$ cd ~/Destktop/logging-config/solution
$ python calculator.py
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): sans.org:80
DEBUG:urllib3.connectionpool:http://sans.org:80 "GET / HTTP/1.1" 301 0
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): sans.org:443
DEBUG:urllib3.connectionpool:https://sans.org:443 "GET / HTTP/1.1" 301 0
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): www.sans.org:443
DEBUG:urllib3.connectionpool:https://www.sans.org:443 "GET / HTTP/1.1" 200 18737
WARNING:calculator.support_functions:Internet Confirmed.
WARNING:calculator.support_functions:Adder object exported!
DEBUG:calculator:Adding 10 and 5
WARNING:calculator.support_functions.adder:Set initial value to 0
INFO:calculator.support_functions.adder:Adding values (10, 5)
INFO:calculator.support_functions.adder:Sending the result!
WARNING:calculator:The result is 15
```

It should also write the following file to /tmp/calculator.log:

```
$ cat /tmp/calculator.log 
WARNING:calculator.support_functions:Internet Confirmed.
WARNING:calculator.support_functions:Adder object exported!
WARNING:calculator.support_functions.adder:Set initial value to 0
WARNING:calculator:The result is 15
```

## Submitting your answer

Only submit the log.config file.
>>> d.solution("~/Desktop/bonus-logging-config/solution/log.config")
