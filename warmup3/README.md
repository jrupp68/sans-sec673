Most of the questions in SEC673 require that you submit your code to the server. A README.md file, similar to this, will explain what you have to do to score the points.

For this question, you need to write a simple module that implements two functions. The module must be named `solution.py`.

You will upload your completed code to the pywars server using the .solution() method. The server will use the unit test module to evaluate your code and show you the results. The folder containing this file also contains a copy of the program used by the server to evaluate your code. You will not normally receive a copy of the test but rather will have to pass the path to your source code to the .solution() method. For example, `d.solution('/path/to/solution.py')` will submit your code and show you the results of the test. For this first lab, you can try it locally to understand what the server is doing.  The program `test.py` will `import solution` and call your functions to evaluate the code. Run the unit test program by typing `python3 test.py` and you will see the results. Once you get solution.py working properly, upload the finished version using the `.solution()` method.

To complete this challenge, `solution.py` must contain two functions. The first is named add() and the second is named addmany().

### add()
function `add()` should take in 2 numbers, add them together and return the result.
For example, `add(10,15)` should return 25.

### addmany()
The second function is called `addmany()`. It should take an undefined number of arguments.
It should add together each of the arguments and return the result.
- `addmany(1,2)` should return 3 
- `addmany(10,15,20)` should return 45
- `addmany(1,1,1,1,1,1,1)` should return 7

Once this program passes all of the tests, call .solution() and pass the absolute path to the your `solution.py` script. For example, `d.solution('/home/student/Desktop/warmup3/solution.py')`

