# In this lab, you must automatically complete your Intro to Computer Science Homework.

---

This may or may not be a real situation. The names of individuals, schools and assignments have been changed to protect the innocent.

School XYZ requires their Introduction to Computer Science students to SSH into a remote server to complete specific homework assignments. One of the assignments requires that, "for practice", you convert 100 binary numbers into hexadecimal. If you get one wrong, you must start over. After one or two tries, you decide to apply your advanced computer science skills to complete this annoying homework assignment. You decide to write a small program to automatically connect, read the binary values, convert them to hex, and submit the correct answer.

In this lab, rather than making you SSH into the target, I am giving you the program that ran on the remote server. You have been told that after 100 iterations, it will give you a flag that you must turn in to the instructor. Obviously in our scenario, you can just read the flag from the source code, but in the original remote scenario, this is not possible. Write a Python program to launch 'homework.py' script and answer all of the questions. 'homework.py' must be in the same directory as your program.

To get started, use pexpect spawn to launch homework. You must pass any arguments that are passed to solution.py to homework.py and then interact with homework.py. In the SSH environment, the students' login name was passed as an argument to homework.py. This made each students flag given to them after completing the lab unique so that they could not share the flag with one another. Your solution.py should accept a command line argument and pass it on to homework.py to facilitate this functionality. When you launch homework.py, it will look something like this:


```
client = pexpect.spawn('python3 homework.py '+sys.argv[1])
```

Retrieve the flag and print it.


---

## Example Manually Running homework.py

It may help you understand the problem if you try `homework.py` manually. After answering a few question hit CONTROL-C to exit.
```
$ python3 homework.py myloginname
To complete this exercise you must correctly convert 100 binary numbers to hexadecimal.
Convert the following binary to hexidecimal.
 Binary: 0b10110110
    Hex: 0xB6
Correct.  You have completed 1 of 100.
Convert the following binary to hexidecimal.
 Binary: 0b01111000
    Hex: 0x78
Correct.  You have completed 2 of 100.
Convert the following binary to hexidecimal.
 Binary: 0b11110100
    Hex: F4 
Incorrect. You must start over 
Convert the following binary to hexidecimal.
 Binary: 0b10010010
    Hex: 0x92
Correct.  You have completed 1 of 100.
Convert the following binary to hexidecimal.
 Binary: 0b10111100
    Hex: 
CONTROL-C
```

If you continue this process and solve 100 of them, you will get the flag. Perhaps there is an easier way. Use pexpect to launch `homework.py` and enter the solution to each of the challenges.
 
--- 
## Testing your solution.

When executed, your solution must just extract the flag printed at the completion of the homework assignment. Your script will be tested against a program that is almost identical to homework.py. The only difference is how the flag is generated. Collect and print the flag that is printed after you have answered 100 items correctly. Upload your script with the name `solution.py`. When executed, it must print the flag and only the flag. For example, for the homework.py script you are provided, it will produce the following output when given the following arguments.

```
$ python solution.py 1 
894ffc1e83b5e77a3be655cccc7769ec
$ python solution.py 2
4e01aabe5ffd722f21913ea3b289d3d0
$ python solution.py 3
635f9916073be1aa6e6c890a35abddc0

```

---
## Submitting your Solution
Submit your answer by passing the complete path to a single module named solution.py to d.solution() 

```
>>> d.solution("~/Desktop/pexpect-homework/solution.py")
```


