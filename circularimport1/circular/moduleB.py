# Do not modify this script. Any changes made here are ignored by the server.
# You should only modify "moduleA.py".

import circular.moduleA 

class ObjectB(circular.moduleA.ObjectA):
    print(f"ObjectB define")
    def __add__(self, other_value):
        print("Normal addition")
        if isinstance(other_value, circular.moduleA.ObjectA):
            print("Cant add ObjectA to ObjectB")
        return NotImplemented