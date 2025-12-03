class NamedInteger(int):
    def __new__(cls, name, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.name = name
        return instance

    def as_tuple(self):
        return (self.name, self.real)

    def __repr__(self):
        return f"NamedInteger('{self.name}', {self.real})"