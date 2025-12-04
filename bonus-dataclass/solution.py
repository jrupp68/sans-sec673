from dataclasses import dataclass, field

@dataclass
class IPRecord:
    name: str = field(repr=False)
    address: str = field(default="127.0.0.1", repr=False)

    def __repr__(self):
        return f"IPRecord(name='{self.name}')"


if __name__ == "__main__":
    rec_x = IPRecord("server","1.1.1.1")
    print(repr(rec_x))
    print(rec_x.address)
    print(rec_x.name)