In this lab you will go back to your IPRecord class and modify it such that it meets the folowing specification.

Oh sure  anybody can write a Least Recently Used Cache  Just use @functools.lrucache!

Write a Least Frequently Used.
Each item in the cache must track it cache count

With an LRU cache this happens...
buffer_size = 3
cache = functools.lrucache(buffersize=3)
for i in range(10000000)
    cache.get("big count")
cache.get('onecounta')
cache.get('onecountb')
cache.get('onecountc')    <= replaces big count in the cache

So track click tracks.

Create a @lfucache decorator  This is the lease frequently used.   


Here is an example of interacting with your object.

```
>>> x = IPRecord("100.100.100.100")
>>> y = IPRecord("2.2.2.2")
>>> x.address
IPv4Address('100.100.100.100')
>>> str(x)
'100.100.100.100'
>>> x.created
datetime.datetime(2020, 9, 15, 11, 15, 2, 485425)
>>> x == y
False
>>> x != y
True
>>> x > y
True
>>> x < y
False
>>> x <= y
False
>>> x >= y
True
```