# NamedIntegers

## Objective
Build a new class called NamedInteger in `solution.py`.

This object must be a subclass of an integer (int). This new object behaves identically to an integer with the following exceptions.

 - When calling NamedInteger you will include a name as the first argument.  All other arguments are normal integer arguments.
 - The object has a "as_tuple()" method that will convert it to a tuple with the name in the first position and its value in the second.
 - The objects repr() method is updated to "NamedInteger(name, value)"

Note: For this exercise I want to focus your attention on the instanciation and use of self in immutable objects. We will not override any of the normal integer methods.  That means __add__ and other normal integer methods will still return a normal integer. You would need to modify all of the normal integer methods that return integers if we were to use this object in production code, but it is not required for this exercise.

## Example Use
Here is some example use of the object.

```
>>> import solution
>>> x = solution.NamedInteger("course", "2A1", 16)   #2a1 base 16 is 673
>>> type(x)
<class '__main__.NamedInteger'>
>>> isinstance(x, int)
True
>>> x.as_tuple()
('course', 673)
>>> x
NamedInteger('course', 673)
>>> y = solution.NamedInteger("version", "0101", 2)
>>> x.as_tuple() + y.as_tuple()
('course', 673, 'version', 5)
>>> y = y + 10
>>> y
15
>>> type(y)    #Type being int is not ideal, but ok for this lab.
<class 'int'>
>>> y.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'name'
>>> 

```

## Submit your answer
WHen your done submit only solution.py using the .solution() method.
