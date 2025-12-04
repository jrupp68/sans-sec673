
def all_msb_clear(data:bytes) -> bool:
    #When given bytes it will return True if the Most Significant Bit of each byte is unset (cleared).  If an single byte in the bytes has the most significant bit set it must return False.
    for byte in data:
        if byte >= 128: # MSB is set
            return False
    #MSB unset on every byte
    return True

def key_length(data:bytes)-> int:
    #The data contains an encrypted block of data. Lets call that data DATA1. An XOR cypher was used to encrypt DATA1 with KEY1. KEY1 is a fixed length key that is repeated over and over again for the length of DATA1. The clear text data DATA1 was comprised solely of ASCII characters (ie each bytes Most Significant Bit is clear). If you somehow eliminated they key from the data by XORing the data with itself, those bits would be clear again. Remember that if ENC1 = DATA1 ^ KEY1 and ENC2 = DATA2 ^ KEY1 then ENC1^ENC2 = DATA1^DATA2 because KEY1^KEY1 is all zeros. Determine the length of repeating KEY1. This function will return the length of the repeating key.
 
def xor(data:bytes, key:bytes)->bytes:
    #Given data bytes and a key bytes XORs them together and returns the results as bytes. The key may be shorter than the data. In that case the key will be repeated over and over until its length is the same as data.

def all_printable(data:bytes)->bool:
    #Given data bytes it will return True if data is comprised 100% of characters in "string.printable". ie the "printable" string in the "string" module. 

def check_key(data:bytes, key_size:int, key_to_check:bytes, key_offset:int) -> bool:
    
