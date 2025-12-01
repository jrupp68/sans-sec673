# Convert "mymodule.py" into a "mypackage"


## Instructions

In the same folder as this README, you will find a file called mymodule.py. You must convert it into a package called mypackage. It should faithfully reproduce the same functionality as the single module. Begin by creating a new folder named "mypackage" inside the module2package folder on your Desktop.

```
cd ~/Desktop/module2package
mkdir mypackage
```

Create all the required files to turn this directory into a package that performs the same functions as mymodule.py.

---

## Package Details
Your package must contain the following files and folders.  This should be a subdirectory of the module2package folder that this README is in.

- mypackage (directory that contains these files)
    - __main__.py
    - support_functions.py
    - __init__.py

### __main__.py
When executed, mypackage should compute the sum and difference of any command line arguments that are passed to it and print them, as shown below.

### __init__.py
When imported, mypackage should only make the add function available to functions that import it.

### support_functions.py
All functions defined inside of mymodule.py should be placed inside of this file for use in mypackage.

---

## Testing your package

When executed, your package will call the add function and add the values passed on the command line.

```
$ ls
mypackage
$ python3 -m mypackage 100 200
The sum is 300
The difference is -100
```
   
When imported, your package must only publish the add function.

```
$ ls
mypackage
$ python
>>> import mypackage
>>> mypackage.add(100,200)
300
>>> mypackage.sub(100,200)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mypackage' has no attribute 'sub'
```

We should be able to import the support_functions module that contains all the functions from mymodule.py.

```
$ ls
mypackage
$ python
>>> import mypackage.support_functions
>>> mypackage.support_functions.sub(100,200)
-100

```

---

## Submit your answer

The .solution() function can be given either a single file or a directory. In this case, you should submit the entire folder that contains the 'mypackage' directory. For example, if you created the "mypackage" directory on your /home/student/Desktop/module2package folder, then you would submit it by running .solution("/home/student/Desktop/module2package").  
