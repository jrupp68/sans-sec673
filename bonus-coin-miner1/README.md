# Bonus Coin Miner

## Objective

You must develop a function to mine a crypto coin. The process of mining a bitcoin starts with the hash of the previous "block". To successfully mine a coin you must add a value to the hash of the previous block and produce a valid hash for the next crypt block. Your hash qualifies as a valid hash if and only if it is not the same as the hash of the previous block and the first few bits are all set to zero.  The number of required zero bits will vary depending upon the difficulty desired. Here is an example of a hash where the first three bytes (24 bits) are zero.

`000000ea33a65f09ed56b78c96a8a591c2abff6bfa360212a3152ca204ed4889`

As an FYI: Yes. That is a simple version of how "proof of work" mining really works in bitcoin.  The hash of the very first bitcoin blocks required that the first 4 bytes (or 32 bits) of the hash were all zeros. Then over time to increase scarcity the difficult (aka the number or zeroes) has increased.  Today at least 9 bytes or 72 bit must be set to zero. 

https://en.bitcoin.it/wiki/Genesis_block

Note: We have made this challenge easier than mining a coin by choosing fewer zeroes. This was done so as not to require weeks of time or as much electricity as a small country consumes in a year to mine a single coin and solve this challenge. 

https://cbeci.org/


## Functions

You must write a function that will confirm that a new bit if data will produce a new valid block chain.   

`def confirm_next_key(previous_block:bytes, new_key:bytes,  difficulty:int) -> bool:`

Create a function called `confirm_next_key()`.  The function will take in the previous_block hash, a possible new key, and a difficulty. The previous_block will be a sha256 hash of the last confirmed block in the chain.  The new_key will be a proposed set of bytes where the sha256 hash of those bytes concatenated to the end of the previous_block will have the specified number of leading bits set to zero. The diffulculty will be the number of leading (most significant) bits that must be zero for the key to be confirmed. The difficulty will be a number between 1 and 255. This function will return True if the the sha256 hash of `previous_block + new_key` begins with the required number of leading zeroes.  It will return False if it does not or if `previous_block + new_key` is the same as `previous_block`.

## Example use

Here is an example set of data you can use to test your function.

```
>>> previous_block
b'00000060aef92376fabf3ee09de2c11e2f5da458b936498089cfc1ed289c9830'
>>> confirm_next_key(previous_block, b'\x01:\xff\xb2', 24)
True
>>> confirm_next_key(previous_block, b'', 1)
False
>>> confirm_next_key(previous_block, b'\x01:\xff\xb3', 24)
False
>>> confirm_next_key(previous_block, b'\x01:\xff\xb2', 20)
True
>>> confirm_next_key(previous_block, b'\x01:\xff\xb2', 26)
False
```

Here is another set of data you can use to test your function.

```
>>> previous_block
b'000000f9b79b2ec070ac8e51f724a6fba96d621b97a471ecbbc653e765249368'
>>> confirm_next_key(previous_block, b'\x02\x90\xeb', 16)
True
>>> confirm_next_key(previous_block, b'\x1d\x84\xb4', 16)
True
>>> confirm_next_key(previous_block, b'\x1d\xa6\xe2', 16)
True
>>> confirm_next_key(previous_block, b'\x1d\xa6\xe3', 16)
False
```


## Submitting your solution.

When you are finished with your function you should submit the path to solution.py.

```
>>> d.solution("~/Desktop/bonus-coin-miner1/solution.py")

```




```