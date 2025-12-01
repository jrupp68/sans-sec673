Continue building on the solution module from an earlier exercise.

To complete this challenge `solution.py` must contain the previous two functions `add()` and `addmany()` from the earlier exercise as well as the following enhancements.

In addition your module must detect if it is being executed or if it is being imported.
 - If it is imported it should make the `add()` and `addmany()` function available just as it did before
 - If it is executed it should look for command line arguments. Each white space separated numeric value on the command line must be summed.
 - Do not use any separator other than white space.  For example, do not split on colons.
 - Any numeric values should be converted to floats and added.
 - Any non-numeric numbers on the command line must be ignored.
 - The output will always be a float.


### Here is an example of your script in use
```
>>> import solution
>>> solution.add(100,200)
300
>>> solution.addmany(1,2,3)
6

$ python3 solution.py 1 2.5 3 
6.5
$ python3 solution.py 1 NotAnumber 3.0 
4.0
$ python3 solution.py 
0.0
$ python3 solution.py 1,2,3 4.5 2
6.5

```

To see if your code is correct submit `solution.py` script.  For example `d.solution('/home/student/Desktop/warmup5/solution.py')`

