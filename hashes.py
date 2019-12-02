import time
import hashlib
#import bcrypt

key = b"hello" # b flag makes it a bye string which is needed if you want to has it

print(hashlib.sha256(key).hexdigest())
#hexdigest turns it into a hexidecimal reprisentation



def djb2(key):
    #start from an arbitrarily large prime number
    hash_value = 5381