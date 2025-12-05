In this lab you will implement a decorator that allows you to decorate a function as follows:

`@decorator_factory(5,newval=10)`

The first argument is an integer that will indicate how many times you want to run the decorated function. All other arguments are arguments that will be automatically added to the decorated function when called. Consider this example:

```
@decorator_factory(5,5,10)
def mysum(*args):
    return sum(args)
```

This would decorate the mysum function such that when `mysum(15,20)` is called it would run `mysum(5,10,15,20)` five times. The value returned from the mysum function would be a tuple with two values.  The first is a list with the results from all 5 runs and the second would be the time in required to run the function 5 times. You should measure the time by recording the difference between time. To calculate the time your function must call a function named time.process_time() before and after executing the functions and subtract the ending time from the starting time. For example, `([50,50,50,50,50], 0.002312 )`


```
>>> @decorator_factory(3,[1,2,3,4,5],['a','b','c','d','e'])
... def myzip(*args):
...     return list(zip(*args))
... 
>>> myzip([6,7,8,9,10],['x','y','z'])
([[(1, 'a', 6, 'x'), (2, 'b', 7, 'y'), (3, 'c', 8, 'z')], [(1, 'a', 6, 'x'), (2, 'b', 7, 'y'), (3, 'c', 8, 'z')], [(1, 'a', 6, 'x'), (2, 'b', 7, 'y'), (3, 'c', 8, 'z')]], 2.7699000000019902e-05)
```

#### Submitting your Solution

When you are finished just submit `solution.py`.
