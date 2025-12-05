
def all_msb_clear(data:bytes) -> bool:
    #When given bytes it will return True if the Most Significant Bit of each byte is unset (cleared).  If an single byte in the bytes has the most significant bit set it must return False.
    for byte in data:
        if byte >= 128: # MSB is set
            return False
    #MSB unset on every byte
    return True

def key_length(data: bytes, max_key_len: int = 40) -> int:
    if len(data) < 20:
        return 1

    best_len = 2
    best_score = 0.0

    for length in range(2, max_key_len + 1):
        matches = 0
        for i in range(len(data) - length):
            if (data[i] ^ data[i + length]) < 128:   # MSB cleared → same key byte
                matches += 1
        score = matches / (len(data) - length)

        if score > best_score:
            best_score = score
            best_len = length

    return best_len

def xor(data:bytes, key:bytes)->bytes:
    #Given data bytes and a key bytes XORs them together and returns the results as bytes. The key may be shorter than the data. In that case the key will be repeated over and over until its length is the same as data.
    pass

def all_printable(data:bytes)->bool:
    #Given data bytes it will return True if data is comprised 100% of characters in "string.printable". ie the "printable" string in the "string" module. 
    pass

def check_key(data:bytes, key_size:int, key_to_check:bytes, key_offset:int) -> bool:
    pass

