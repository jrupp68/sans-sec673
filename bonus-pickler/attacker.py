import socket
import pickle
from serialize_me import MyClass

data = pickle.dumps(MyClass())

s = socket.socket()
s.connect(("127.0.0.1", 9000))
print("Sending data")
s.sendall(data)
print(s.recv(65535))
