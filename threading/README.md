# Lab - Threading

## Lab Objectives
In this lab, you will use multi-threading and multi-processing to speed up a slow process in your program.

The program "sniffer/dns_lookups.py" has been written to take advantage of the powerful sniffer module you have developed. It is not intended to be part of your package. The goal of this program is to print packets to the screen, but rather than just printing IP Addresses, it will convert those IP Addresses into DNS hostnames by doing a DNS Reverse lookup. Because that process is slow, you will use various techniques to improve performance.

## Instructions

You are highly encouraged to use the walkthrough in your workbook for this lab. There are multiple files that must be changed and discovering them on your own may be time prohibitive.

The program dns_lookups.py has already been written for you.  It will lookup the DNS hostnames of the source IP address and print that before printing the packet. But it runs very slowly and you need to make it run faster. Be aware that this program only simulates DNS lookups to avoid our class potentially impacting the performance of a shared DNS server in classroom environments. However, the simulated lookup also simulates network delays to provide a good, if not exaggerated, example of why multi-threading is useful. In this lab, we are only looking up the source address, because there is no additional benefit to you, as the student, in making you do both the source and the destination. However, tools such as Wireshark and TCPDUMP will typically do both by default.

If you run the program now, it calls several functions and times them using a @time_this decorator. We will learn how to write decorators later in the course.

```
$ python3.10 dns_lookups.py 
With no enhancements
This function took 53.67945432662964 seconds.
With Multithreading
This function has not been written yet. It does nothing.
This function took 8.821487426757812e-06 seconds.
With Multiprocessing
This function has not been written yet. It does nothing.
This function took 4.5299530029296875e-06 seconds.
With Multithreading map
This function has not been written yet. It does nothing.
This function took 4.76837158203125e-06 seconds.

```

The output tells us that it took nearly a full minute to do our reverse DNS lookups on 100 records without any enhancements. 

In `dns_lookups.py`, you will find three functions. Replace the existing print statements with code that performs function as described below. Run the program again to observe how each of these concurrent programming solutions affects the performance. Then, try adding a Least Recently Used Cache to the reverse_lookup method and check the performance again.

The only thing that should be changed in `dns_lookup.py` are these three functions. The comments inside of each of the functions provide you with additional instructions.

```
@time_this
def with_multi_threading(pkts, print_it=True):
    #Print in any order as fast as they can be resolved with a ThreadPoolExecutor
    #You must use a ThreadPoolExecutor in a context manager
    #You must submit each packet to reverse_lookup
    #You must step through all the results with as_completed() and print them if print_it is True
    print("This function has not been written yet. It does nothing.")

@time_this
def with_multi_processing(pkts, print_it=True):
    #Print in any order as fast as they can be resolved with a ProcessPoolExecutor
    #You must use a ProcessPoolExecutor in a context manager
    #You must submit each packet to reverse_lookup
    #You must step through all the results with as_completed() and print them if print_it is True
    #This will require that Packet objects be pickled correctly
    print("This function has not been written yet. It does nothing.")

@time_this
def with_multi_threading_map(pkts, print_it=True):
    #Print in original packet order using a ThreadPoolExecutor's .map function
    #You must use a ThreadPoolExecutor in a context manager
    #You must map reverse_lookup across all of the packets
    #You must step through all the results and print them if print_it is True
    print("This function has not been written yet. It does nothing.")
```

Additionally, you will have to make changes to Packet() objects such that @lru_cache can be used on reverse_lookup().

## Submit your answer
When you are finished, submit the entire `threading` directory. Only three files that you submit may be changed. You will make changes to `dns_lookups.py`,  `sniffer/packet.py` and `sniffer/prototocols/protocol.py` as needed. Changes to other files will be ignored.

```
>>> d.solution("~/Desktop/threading/")
```