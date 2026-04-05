import hashlib

def get_hash(key):
    return int(hashlib.md5(key.encode()).hexdigest(),16)