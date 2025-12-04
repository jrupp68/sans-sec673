import random
import time
import pathlib
import concurrent.futures
from functools import lru_cache
from sniffer.packetlist import PacketList
from sniffer.filter import Filter

@lru_cache
def reverse_lookup(pkt):
    ip = pkt['IP'].ip_src
    wordlist_path = pathlib.Path("/home/student/Desktop/sans-sec673/threading/wordlist.txt")
    wordlist = wordlist_path.open("rt").readlines()
    tlds = [ "org","com","gov","edu" ]
    time.sleep(random.random())
    host = f"{random.choice(wordlist)}.{random.choice(wordlist)}.{random.choice(tlds)}".replace("\n","")
    return host, pkt

def time_this( func_to_decorate ):
    def func_factory(*args,**kwargs):
        start_time = time.time()
        result = func_to_decorate(*args,**kwargs)
        elapsed = time.time() - start_time
        print(f"This function took {elapsed} seconds.")
        return result
    return func_factory

@time_this
def no_enhancements(pkts, print_it=True):
    #This version has no speed enhancements
    #It steps through each packet and does a reverse lookup
    #If print_it is True it prints the results.
    for pkt in pkts: 
        hostname,pkt = reverse_lookup(pkt)
        if print_it:
            print(f"{hostname} : {pkt}")

@time_this
def with_multi_threading(pkts, print_it=True):
    #Print in any order as fast as they can be resolved with a ThreadPoolExecutor
    #You must use a ThreadPoolExecutor in a context manager
    #You must submit each packet to reverse_lookup
    #You must step through all the results with as_completed() and print them if print_it is True
    
    running_threads = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for pkt in pkts:
            running_threads.append(executor.submit(reverse_lookup, pkt))
        for each_result in concurrent.futures.as_completed(running_threads):
            hostname, packet = each_result.result()
            if print_it:
                print(f"{hostname} : {packet}")

  
@time_this
def with_multi_processing(pkts, print_it=True):
    #Print in any order as fast as they can be resolved with a ProcessPoolExecutor
    #You must use a ProcessPoolExecutor in a context manager
    #You must submit each packet to reverse_lookup
    #You must step through all the results with as_completed() and print them if print_it is True
    #This will required that Packet objects be pickled correctly
    
    running_threads = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        for pkt in pkts:
            running_threads.append(executor.submit(reverse_lookup, pkt))
        for each_result in concurrent.futures.as_completed(running_threads):
            hostname, packet = each_result.result()
            if print_it:
                print(f"{hostname} : {packet}")

@time_this
def with_multi_threading_map(pkts, print_it=True):
    #Print in original packet order using an ThreadPoolExecutors .map function
    #You must use a ThreadPoolExecutor in a context manager
    #You must map reverse_lookup across all of the packets
    #You must step through all the results and print them if print_it is True
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for hostname, pkt in executor.map(reverse_lookup,pkts):
            if print_it:
                print(f"{hostname} : {pkt}")

if __name__ == "__main__":    
    pkts = PacketList()
    pkts.capture_filter = Filter("IP","ip_svc", list(range(256)))
    pkts.rdpcap("/home/student/Desktop/sans-sec673/threading/web.pcap")
    # Will just do the first 100 packets
    pkts = pkts[:100]
    print("With no enhancements")
    no_enhancements(pkts, False)
    print("With Multithreading")
    with_multi_threading(pkts, False)
    print("With Multiprocessing")
    with_multi_processing(pkts, False)
    print("With Multithreading map")
    with_multi_threading_map(pkts, False)