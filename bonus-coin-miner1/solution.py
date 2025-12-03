import hashlib

def confirm_next_key(previous_block: bytes, new_key: bytes, difficulty: int) -> bool:
    """
    Validate if appending new_key to previous_block produces a valid next block
    under the given difficulty (number of leading zero BITS in the SHA-256 hash).

    Rules:
    - Compute SHA-256 of (previous_block + new_key)
    - The resulting hash must have at least 'difficulty' leading zero bits
    - The new hash MUST NOT be identical to previous_block
    - difficulty is between 1 and 255

    Args:
        previous_block: 32-byte SHA-256 hash of the previous block
        new_key: candidate nonce/data to append
        difficulty: number of leading zero bits required

    Returns:
        bool: True if valid proof-of-work, False otherwise
    """
    if new_key == b'':
        return False
    
    if not (1 <= difficulty <= 255):
        raise ValueError("Difficulty must be between 1 and 255")

    # Concatenate previous block hash + candidate key
    data = previous_block + new_key

    # The hash must be different from the previous block
    new_hash = hashlib.sha256(data).digest()

    if new_hash == previous_block:
        return False

    # Count leading zero bits in the hash
    # We go byte by byte, then bit by bit
    zero_bits = 0
    for byte in new_hash:
        if byte == 0:
            zero_bits += 8
        else:
            # Count leading zeros in this byte
            for bit in range(7, -1, -1):
                if (byte & (1 << bit)) == 0:
                    zero_bits += 1
                else:
                    break
            break  # Stop after first non-zero byte

    return zero_bits >= difficulty


# === TEST CASES ===
if __name__ == "__main__":
    # Test set 1
    previous_block1 = b'00000060aef92376fabf3ee09de2c11e2f5da458b936498089cfc1ed289c9830'
    assert confirm_next_key(previous_block1, b'\x01:\xff\xb2', 24) == True
    assert confirm_next_key(previous_block1, b'', 1) == False
    assert confirm_next_key(previous_block1, b'\x01:\xff\xb3', 24) == False
    assert confirm_next_key(previous_block1, b'\x01:\xff\xb2', 20) == True
    assert confirm_next_key(previous_block1, b'\x01:\xff\xb2', 26) == False

    previous_block = b'000000f9b79b2ec070ac8e51f724a6fba96d621b97a471ecbbc653e765249368'
    assert confirm_next_key(previous_block, b'\x02\x90\xeb', 16) == True
    assert confirm_next_key(previous_block, b'\x1d\x84\xb4', 16) == True
    assert confirm_next_key(previous_block, b'\x1d\xa6\xe2', 16) == True
    assert confirm_next_key(previous_block, b'\x1d\xa6\xe3', 16) == False

    print("All tests passed!")