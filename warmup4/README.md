Continue building on the solution from your previous question. This time, you are not given the unit test that is used by the server. You could develop your own small unit test to test your code. Alternatively, you can just upload it and see what the server says.

Start by copying your completed `solution.py` from the previous challenge (warmup3) into your warmup4 directory.

To complete this challenge, `solution.py` must still contain the previous two functions `add()` and `addmany()`. However, it must also contain the new functions below. Many labs will build on the previous lab, and you should not remove functionality unless told to do so.

Add the following functions to your `solution.py` module.


### bytes_to_str(inbytes:bytes) -> str
This function will receive a bytes string that contains a UTF-8 string. Turn it into a string and return the string.

### str_to_bytes(instr:str) -> bytes
Given a string, turn it into bytes.

### byte_length(utf8_char:str) -> int
Given a string that contains UTF-8 encoded characters, return the number of bytes required to store that character.



### Here is an example of your script in use
```
>>> import solution
>>> solution.bytes_to_str(b'hello')
'hello'
>>> solution.str_to_bytes('hello')
b'hello'
>>> solution.byte_length('a')
1
>>> solution.byte_length('🐍')
4
```

To see if your code is correct, submit the `solution.py` script. For example, `d.solution('/home/student/Desktop/warmup4/solution.py')```

