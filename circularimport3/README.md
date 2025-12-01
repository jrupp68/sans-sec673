# Circular Import 3

## Description

Our SPF100 tool kit has a second circular reference in it. This time, it is in the base64 utility program. Find it and fix it!


## Overview

Our base64 utility works fine when we run it as a module.

```
$ python -m utils.base64 BASE64encodeMEpython 
QkFTRTY0ZW5jb2RlTUVweXRob24=
```
Here, it dutifully encodes "Base64encodeMEpython" and generates the response. However, when we try to run this as a program it does not work.

```
$ python utils/base64.py BASE64encodeMEnow
Traceback (most recent call last):
  File "/home/student/Desktop/circularimport2/utils/base64.py", line 14, in <module>
    print(base64_decode(cli_data))
  File "/home/student/Desktop/circularimport2/utils/base64.py", line 8, in base64_decode
    return codecs.decode(data.encode(), "base64").decode()
  File "/usr/lib/python3.10/encodings/base64_codec.py", line 19, in base64_decode
    return (base64.decodebytes(input), len(input))
AttributeError: module 'base64' has no attribute 'decodebytes'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/student/Desktop/circularimport2/utils/base64.py", line 16, in <module>
    print(base64_encode(cli_data))
  File "/home/student/Desktop/circularimport2/utils/base64.py", line 5, in base64_encode
    return codecs.encode(data.encode(),"base64").decode()
  File "/usr/lib/python3.10/encodings/base64_codec.py", line 15, in base64_encode
    return (base64.encodebytes(input), len(input))
AttributeError: module 'base64' has no attribute 'encodebytes'
```

This syntax should work and produce the same output as when it is run as a module. Resolve this import error.

## Submitting the solution.

Like the other circular imports, solving this will only require one change to a single file. The one file you should be changing is in the `utils` folder. I am not telling you the name of the file. When you are finished, you will submit that one file. 


```
d.solution("~/Desktop/circularimport2/utils/THE-CORRECTED-FILE.py")
Correct!
```



