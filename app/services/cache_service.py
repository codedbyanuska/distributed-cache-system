from app.cache.cache_cluster import CacheCluster
from app.db.db import Database

class CacheService:
    def __init__(self):
        self.cache=CacheCluster()
        self.db=Database()
    
    def get(self,key):
        value=self.cache.get(key)

        if value is not None:
            print("Cache Hit")
            return value
        
        print("Cache Miss")
        value=self.db.get(key)

        if value is not None:
            self.cache.set(key,value, ttl=60)

        return value
    
    def set(self,key,value):
        #Write to DB first
        self.db.set(key,value)

        #Then update cache
        self.cache.set(key,value,ttl=60)

        return {"message": "Key stored successfully"}
    
    def delete(self,key):
        self.db.delete(key)
        
        self.cache.delete(key)

        return {"message": "Key deleted successfully"}
