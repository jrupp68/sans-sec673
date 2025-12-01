class ObjectA(object):
    print("ObjectA define")

    def __init__(self):
        print(f"{self.__class__.__qualname__} initialized")

    def __radd__(self, other_value):
        import circular.moduleB

        print("Reflected addition")
        if isinstance(other_value, circular.moduleB.ObjectB):
            print("Cant add ObjectB to ObjectA")
            return "Addition Attempted"
        return NotImplemented
