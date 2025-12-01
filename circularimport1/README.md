# Fix the Circular Import 1

## Instructions

The package named "circular" contains a circular reference. You must fix the circular reference. **You are only permitted to modify the program "moduleA.py" inside of the circular folder.**

The directory structure looks like this:

```
$ tree circular/
circular/
├── __main__.py
├── moduleA.py
└── moduleB.py
```
When you execute the program as a module, it does not import correctly.

```
$ cd ~/Desktop/circularimport1
$ python -m circular
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/student/Desktop/circularimport1/circular/__main__.py", line 1, in <module>
    import circular.moduleA   
  File "/home/student/Desktop/circularimport1/circular/moduleA.py", line 1, in <module>
    import circular.moduleB
  File "/home/student/Desktop/circularimport1/circular/moduleB.py", line 3, in <module>
    class ObjectB(circular.moduleA.ObjectA):
AttributeError: module 'circular' has no attribute 'moduleA'
```


## Test Your Package

When you have finished, the program should run successfully. The output will look like this:

```
$ python -m circular
ObjectA define
ObjectB define
ObjectA initialized
ObjectB initialized
Normal addition
Cant add ObjectA to ObjectB
Reflected addition
Cant add ObjectB to ObjectA
Addition Attempted
```

## Submit your answer

You will only submit your modified copy of "moduleA.py".

```
>>> d.solution("~/Desktop/circularimport1/circular/moduleA.py")
Correct! 
```

Note: Additional information about the test will be printed after correct.
