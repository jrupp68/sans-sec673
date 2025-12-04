import pexpect
import re
import sys

client = pexpect.spawn('python3 homework.py '+sys.argv[1])

client.expect("\r\n")
print(client.before)
client.expect("\r\n")
print(client.before)
client.expect("\r\n")
print(client.before)
