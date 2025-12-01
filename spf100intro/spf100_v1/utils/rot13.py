import sys
import codecs

def rot13_encode(data):
    return codecs.encode(data,"rot13")

def rot13_decode(data):
    return codecs.decode(data, "rot13")

if __name__ == "__main__":
    print(rot13_encode(sys.argv[1]))