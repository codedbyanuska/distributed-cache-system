import time

class CacheNode:
    def __init__(self):
        # This dictionary stores key -> (value, expiry_time)
        self.store= {}

    def set(self,key,value,ttl=None):
        expiry_time=None

        if ttl:
            expiry_time=time.time() + ttl
            
        self.store[key] = (value,expiry_time)

    def get(self, key):
        if key not in self.store:
            return None
        
        value,expiry_time = self.store[key]

        if expiry_time and time.time() > expiry_time:
            del self.store[key]
            return None
        
        return value
    
    def delete(self,key):
        if key in self.store[key]:
            del self.store[key]

