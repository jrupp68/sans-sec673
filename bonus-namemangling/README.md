# NameMangling

## Introduction
The module named solution in this same folder does not function as expected. If you run it you get the following output:

```
cd ~/Desktop/bonus-namemangling
python -m solution
SERVICE: dns was found on port 53 on HOST: dns at address 8.8.8.8
SERVICE: dns was found on port 53 on HOST: dns at address 4.4.4.4
```

But we were expecting the following output:
```
python -m solution
SERVICE: dns was found on port 53 on HOST: google at address 8.8.8.8
SERVICE: dns was found on port 53 on HOST: att at address 4.4.4.4
```

Resolve the issue using Python's name mangling capabilities to make the attributes unique to 'self'.

When you are finished submit the the path to the 'bonus-namemangling' folder that contains the solution module using .solution() to have your code evaluated.

```
>>> d.solution("~/Desktop/bonus-namemangling")
Correct! 
test_IPRecordNameMangling (test.TestSolution) ... ok
test_ServiceResults (test.TestSolution) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
