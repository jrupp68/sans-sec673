import pexpect
import re
import sys

client = pexpect.spawn('python3 homework.py '+sys.argv[1])
for _ in range(100):
    client.expect("Hex:")
    question = client.before
    binary = re.findall(rb"0b(\d{8})", question)[0]
    integer = int(binary,2)
    # answer = hex(integer) doesn't provide padding
    answer = f"0x{integer:02x}"
    client.sendline(answer)
# client.expect("\r\n")
# print(client.before)
# client.expect("\r\n")
# print(client.before)
# client.expect("\r\n")
# print(client.before)
# response = client.before
response = client.read(10240)
# print(response)
flag = re.findall(rb"The flag is '(.*?)'", response)[0]
print(flag.decode())