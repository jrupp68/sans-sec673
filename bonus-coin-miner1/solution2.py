import hashlib
from typing import Tuple, List

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


def mine_next_key(previous_block: bytes, difficulty: int) -> bytes:
    """
    Mines a valid nonce (key) such that:
        SHA256(previous_block + key) has at least 'difficulty' leading zero bits
    Starts from nonce = 0 and increments.
    Returns the key (as bytes) that satisfies the condition.
    """
    nonce = 0
    while True:
        key = nonce.to_bytes((nonce.bit_length() + 7) // 8 or 1, 'big')
        if confirm_next_key(previous_block, key, difficulty):
            return key
        nonce += 1


def next_block_key(previous_block_hex: bytes, difficulty: int) -> Tuple[bytes, bytes]:
    """
    Helper that returns (key, new_block_hash) for debugging/visualization.
    Not required for answer, but matches the example usage.
    """
    key = mine_next_key(previous_block_hex, difficulty)
    new_hash = hashlib.sha256(previous_block_hex + key).digest()
    return key, new_hash.hex()


def mine_three_keys(start_block: bytes, difficulty: int) -> Tuple[bytes, bytes, bytes]:
    """
    Mines three consecutive valid keys starting from start_block.
    Returns a tuple of three keys (as bytes).
    """
    block = start_block
    key1 = mine_next_key(block, difficulty)
    block = hashlib.sha256(block + key1).digest()

    key2 = mine_next_key(block, difficulty)
    block = hashlib.sha256(block + key2).digest()

    key3 = mine_next_key(block, difficulty)

    return (key1, key2, key3)


# === MAIN SOLUTION FUNCTION ===
def solution() -> List[Tuple[bytes, bytes, bytes]]:
    """
    This is the function you submit.
    It processes the .data() content and returns the required list of key tuples.
    """
    # This is the actual data from d.data('bonus-coin-miner2')
    challenges = [
        (bytes.fromhex('000000a116142a248c18c0b3d66a6416af792046c54865ec09f51f457fce0ffe'), 20),
        (bytes.fromhex('0000000000d9a725b1454203960fd6d515f565416e8c3088218742acefc441a5'), 26),
    ]

    # challenges = [
    #     (b'\x00\x00\x00\xfd\x13\xeb\xaeyD\xbd\xc4\x16\x92\xa4\xfco\x871962\xa2\xf4\xc1\x07H\xb7h4WL\xf4', 20), 
    #     (b'\x00\x00\x00\x00\x00\xaa<\x89\xa8>\xfb\x97\xaar\xbe\x82(\x08y\xce\xda\x8cx\x1a\xc9\xbf\x1b\xb2\xacp\xccn', 26)
    # ]
    

    answer = []
    for prev_block, diff in challenges:
        keys = mine_three_keys(prev_block, diff)
        answer.append(keys)
        print(f"Difficulty {diff}: Found keys -> {keys}")

    return answer


# === Run it ===
if __name__ == "__main__":
    result = solution()
    print("\nFinal answer:")
    for i, keys in enumerate(result):
        print(f"  {keys}")