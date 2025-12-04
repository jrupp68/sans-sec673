import random
import sys
import hashlib
import hmac


print("To complete this exercise you must correctly convert 100 binary numbers to hexadecimal.")

correct = 0
while correct <= 99:
    num = random.randint(0,255)
    bin = f"0b{num:08b}"
    hex = f"0x{num:02X}".upper()
    print("Convert the following binary to hexadecimal.")
    print(f" Binary: {bin}")
    answer = input("    Hex: ")
    if answer.upper() == hex:
        correct +=1
        print(f"Correct.  You have completed {correct} of 100.")
    else:
        print("Incorrect. You must start over ")
        correct = 0

flag = hmac.new(b"PassPhrase",sys.argv[1].encode(),hashlib.md5).hexdigest()

print(f"Well done.  You completed the assignment. The flag is '{flag}'.")

    