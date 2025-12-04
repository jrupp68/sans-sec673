 # Bonus Crypto 1 

You must develop a library of functions to identify weaknesses in encryption implementations.   You will write the following functions that perform the following tasks.

 ## Functions

### def all_msb_clear(data:bytes) -> bool:

When given bytes it will return True if the Most Significant Bit of each byte is unset (cleared).  If an single byte in the bytes has the most significant bit set it must return False.

### def key_length(data:bytes)-> int:

The data contains an encrypted block of data. Lets call that data DATA1. An XOR cypher was used to encrypt DATA1 with KEY1. KEY1 is a fixed length key that is repeated over and over again for the length of DATA1. The clear text data DATA1 was comprised solely of ASCII characters (ie each bytes Most Significant Bit is clear). If you somehow eliminated the key from the data by XORing the data with itself, those bits would be clear again. Remember that if ENC1 = DATA1 ^ KEY1 and ENC2 = DATA2 ^ KEY1 then ENC1^ENC2 = DATA1^DATA2 because KEY1^KEY1 is all zeros. Determine the length of repeating KEY1. This function will return the length of the repeating key.
 
### def xor(data:bytes, key:bytes)->bytes:

Given data bytes and a key bytes XORs them together and returns the results as bytes. The key may be shorter than the data. In that case the key will be repeated over and over until its length is the same as data.

### def all_printable(data:bytes)->bool:

Given data bytes it will return True if data is comprised 100% of characters in "string.printable". ie the "printable" string in the "string" module. 

### def check_key(data:bytes, key_size:int, key_offset:int, key_to_check:bytes): -> bool
 - data is the encrypted data
 - key_size is the size of the encryption key used on the data
 - key_to_check is a suspected part of the key that was used to encrypt data. This will be <= key_size
 - key_offset is the position of key_to_check inside the key

  This function breaks data into key_size size chunks. It then uses xors to decrypt a substring of the first chunk at position key_offset of length len(key_to_check) with key_to_check. It will repeat this process for every chunk in the data. If the all of the decrypted substrings are 100% comprised of printable chaacters then this function will return True indicating that you might have just found a part of the key.


 ## Example Usage:
 
```
>>> import solution
>>> solution.all_msb_clear(data)
True
>>> solution.key_length(data)
4096
>>> solution.all_printable(b"abcdefg")
True
>>> solution.all_printable(b"abcd\xe0fg")
False
>>> data = xor(b"abcdefghijklmnopqrstuvwxuz",b"THEKEY")
>>> solution.key_length(data)
6
>>> solution.check_key(data,6,3,b"KEY")
True
>>> solution.check_key(data,6,0,b"THE")
True


```
