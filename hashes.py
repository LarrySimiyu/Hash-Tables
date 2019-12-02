import time
import hashlib
#import bcrypt

key = b"hello" # b flag makes it a bye string which is needed if you want to has it

sha256key = hashlib.sha256(key)
print(hashlib.sha256(key).hexdigest())
#hexdigest turns it into a hexidecimal reprisentation



def djb2(key):
    #start from an arbitrarily large prime number
    hash_value = 5381

    # bit-shift and sum value for each character

    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value

print(djb2(key))

djb2key = djb2(key)

#print(f"sha256 key: {int(sha256key, 0) % 10}")
print(f"djb2 key: {djb2key % 10}")
#turns the key into an integer that is within a specific range 
#and can do that to use it to put things into 
#and take them out of our array