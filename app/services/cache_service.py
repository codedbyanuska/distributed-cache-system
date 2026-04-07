from app.cache.redis_client import RedisClient
from app.db.db import Database
from app.utils.logger import logger

class CacheService:
    def __init__(self):
        self.cache=RedisClient()
        self.db=Database()
    
    def get(self,key):
        value=self.cache.get(key)

        if value is not None:
            logger.info(f"Cache Hit for key: {key}")
            return value
        
        logger.info(f"Cache Miss for key: {key}")
        
        value=self.db.get(key)

        if value is not None:
            self.cache.set(key,value, ttl=60)
            logger.info(f"Key {key} stored in cache")

        return value
    
    def set(self,key,value):
        #Write to DB first
        self.db.set(key,value)

        #Then update cache
        self.cache.set(key,value,ttl=60)

        logger.info(f"Key {key} stored in DB and cache")

        return {"message": "Key stored successfully"}
    
    def delete(self,key):
        self.db.delete(key)
        
        self.cache.delete(key)

        logger.info(f"Key {key} deleted from DB and cache")

        return {"message": "Key deleted successfully"}
