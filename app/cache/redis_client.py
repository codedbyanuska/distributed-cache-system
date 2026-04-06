import redis

class RedisClient:
    def __init__(self):
        try:
            self.client=redis.Redis(
                host='localhost',
                port=6379,
                decode_responses=True
            )
            #Test connection
            self.client.ping()
            print("Connected to Redis")
        except Exception as e:
            print("Redis connection failed",e)
    
    def set(self,key,value,ttl=None):
        if ttl:
            self.client.setex(key,ttl,value)
        else:
            self.client.set(key,value)
    
    def get(self,key):
        return self.client.get(key)
    
    def delete(self,key):
        self.client.delete(key)