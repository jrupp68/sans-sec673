# Time Log Decorator

In this lab, you will implement a decorator that times the execution of a function.

## Instructions

In this lab, you must create a decorator named "@timer_log" inside of `solution.py`. The decorator records the start time, executes the function it is decorating, records the stop time and calculates the total elapsed time. 

The decorated function will have an attribute named .exec_times attached to it. This attribute will store up to the 10 last execution times of the function. This variable can only hold at most 10 values. If an 11th time is added, then the oldest execution time is automatically deleted.  Use a collections.deque for this data structure.

To retrieve the history of times, you will use a .times() function that is attached to the decorated function. The decorated function's .time() function should return a list of up to the last 10 execution times of the function.


### Example Usage

Here is an example of using the @timer_log decorator on a simple function that sleeps for the specified number of seconds.

```
>>> import solution
>>> @solution.timer_log
... def sleep(seconds):
...     time.sleep(seconds)
... 
>>> sleep(2)
>>> sleep(0.2)
>>> sleep.times()
[2.003019332885742, 0.20150136947631836]
>>> sleep.exec_times.append(900.8)
>>> sleep.times()
[2.003019332885742, 0.20150136947631836, 900.8]
>>> for i in range(20000):
...     sleep.exec_times.append(3.14)
... 
>>> len(sleep.exec_times)
10
```

### Submitting your solution

When you have completed the solution, you should submit `solution.py`.