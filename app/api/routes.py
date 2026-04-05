from fastapi import APIRouter
from app.services.cache_service import CacheService

router= APIRouter()

cache_service=CacheService()

@router.get("/cache/{key}")

def get_value(key: str):
    value=cache_service.get(key)

    if value is None:
        return {"message": "Key not found"}
    
    return {"key":key, "value":value}

@router.post("/cache")

def set_value(key: str, value:str):
    return cache_service.set(key,value)

@router.delete("/cache/{key}")

def delete_value(key: str):
    return cache_service.delete(key)