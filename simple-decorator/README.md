# Simple Decorator

In this lab, you will implement a decorator that asserts that only lists are passed as inputs to a function or returned by the function.

## Instructions

Your decorator must be called `@only_lists`.

It will evaluate all of the arguments passed to the decorated function and confirm they are either lists or a descendant of lists. If any argument is not, it will raise an AssertionError. Your decorator does not need to do any processing on the keyword arguments passed to the decorated function. It should pass those on to the decorated function without modification.

The decorator must also evaluate the value returned by the decorated function. If it is not a list or a descendant of a list, it will raise an AssertionError.


## Example Usage

```
>>> @only_lists
... def add_lists(a,b):
...     return a + b
... 
>>> @only_lists
... def add_lists_as_tuple(a,b):
...     return tuple( a + b )
... 
>>> #These should work without error since the arguments are lists.
>>> print( add_lists([1,2,3], [4,5,6]) )
[1, 2, 3, 4, 5, 6]
>>> print( add_lists(b = [1,2,3], a = [4,5,6]) )
[4, 5, 6, 1, 2, 3]
>>> #These should raise errors since they are not lists.
>>> print( add_lists([1,2,3], 12) )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in new_function
AssertionError: The argument must be a list
>>> print( add_lists_as_tuple([1,2,3], [1,2,3]) )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in new_function
AssertionError: The returned value must be a list
```

## Submitting your solution

When you have completed the solution, you should submit `solution.py`.


