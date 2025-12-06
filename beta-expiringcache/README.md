In this lab you will go back to your IPRecord class and modify it such that it meets the folowing specification.

Oh sure  anybody can write a Least Recently Used Cache  Just use @functools.lrucache!

Write a Least Frequently Used.
Each item in the cache must track it cache count

With an LRU cache this happens...
buffer_size = 3
cache = functools.lrucache(buffersize=3)
for i in range(10000000)
    cache.get("big count")
cache.get('onecounta')bonus-pickler
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



import unittest
import solution
import ipaddress
from collections import UserList
import datetime
import pathlib

class TestSolution(unittest.TestCase):

    def test_IPRecord(self):
        x = solution.IPRecord("1.1.1.1")
        self.assertIsInstance(x.address, ipaddress.IPv4Address)
        self.assertIsInstance(x.created, datetime.datetime)
        self.assertEqual(repr(x),"IPRecord('1.1.1.1')")
        with self.assertRaises(ValueError):
            solution.IPRecord("2.2.2.5000")
        self.assertEqual(str(x), "1.1.1.1")

    def test_comparison(self):
        x = solution.IPRecord("1.1.1.1")
        x2 = solution.IPRecord("1.1.1.1")
        y = solution.IPRecord("2.2.2.2")
        y2 = solution.IPRecord("2.2.2.2")
        z = solution.IPRecord("10.10.10.10")
        z2 = solution.IPRecord("10.10.10.10")
        self.assertTrue(z>y>x, "Greater than not working")
        self.assertTrue(x<y<z, "Less than not working")
        self.assertTrue(x==x2, "Equals not working as expected")
        self.assertTrue(x!=y, "Not Equals not working as expected")
        self.assertTrue(z=="10.10.10.10", "Equals not working as expected")
        self.assertTrue(z>=z2>=y>=y2>=x , "Greater than or equal to is not working")
        self.assertTrue(x<=x2<=y<=y2<=z, "Less thank or equal to is not working")
        self.assertFalse(x>y, "Greater than not working")
        self.assertFalse(z<y, "Less than not working")
        self.assertFalse(x==y, "Equals not working as expected")
        self.assertFalse(z=="1.1.1.1", "Equals not working as expected")
        self.assertFalse(x>=y , "Greater than or equal to is not working")
        self.assertFalse(z<=y<=x, "Less thank or equal to is not working")

    def test_uses_modules(self):
        source = pathlib.Path("solution.py").read_text()
        self.assertTrue( "functools" in source, "You need to import functools")
        self.assertTrue( "total_ordering" in source, "You need to decorate your class with total_ordering.")
        print("".join(source.split()).count("def__"))
        self.assertTrue( "".join(source.split()).count("def__") <= 5, "You are only permitted 5 methods in your source code.")