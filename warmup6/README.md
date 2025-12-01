# Warmup6 - File IO

## Objective
Write a program called `solution.py` that takes one command line argument, the name of a file in the same working directory as the program. Your program should open the file, read and analyze the contents. It should do the following:

 - Count the total number of login successes
 - Count the total number of login failures
 - If any IP address fails to login more than one time it should be added to a list of possible attackers
 - Use Python's built in sorted function to sort your list of IP addresses without any key function. ie You will print `sorted(list_of_attackers)`
 - It should print the data in the format shown below.
 - If the file name specified does not exist your program should print `File <name of file> not found.`.

Given this input:
```
LOGIN SUCCESS from 166.131.198.190
LOGIN SUCCESS from 247.75.211.181
LOGIN FAILURE from 33.122.8.44
LOGIN SUCCESS from 199.147.100.220
LOGIN FAILURE from 33.122.8.44
LOGIN FAILURE from 14.219.180.6
```

It should print this output:

```
Login Successes: 3
Login Failures: 3
Possible attacker(s): ['33.122.8.4']
```


## Testing your program

The file infile.txt is provided for you to test your code.  It should produce this exact output.
```
$ python solution.py infile.txt
Login Successes: 104
Login Failures: 96
Possible attacker(s): ['114.83.11.232', '87.159.152.98']
```

Also confirm your file prints the correct error message when asked to process a file that doesn't exist.

```
$ python solution.py notinfile.txt
File notinfile.txt not found.
```

## Submitting your answer
Submit the path to a single file named 'solution.py' to the .solution() method. Your program will be tested against multiple input files that are not provided to you. All input files will be in the same format but will contain different IP Addresses and Login success or failures.

To see if your code is correct submit `solution.py` script.  For example `d.solution('/home/student/Desktop/warmup6/solution.py')`
