
#Must create IPRecord dataclass




if __name__ == "__main__":
    rec_x = IPRecord("server","1.1.1.1")
    print(repr(rec_x))
    print(rec_x.address)
    print(rec_x.name)
    