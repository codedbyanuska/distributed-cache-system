from fastapi import APIRouter, HTTPException
from app.services.cache_service import CacheService

router= APIRouter()

cache_service=CacheService()

@router.get("/cache/{key}")

def get_value(key: str):
    value=cache_service.get(key)

    if value is None:
       raise HTTPException(
           status_code=404,
           detail=f"Key '{key}' not found"
       )
    
    return {"key":key, "value":value}

@router.post("/cache")

def set_value(key: str, value:str):
    try:
        return cache_service.set(key,value)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.delete("/cache/{key}")

def delete_value(key: str):
    try:
        return cache_service.delete(key)
    except Exception as e:
        raise HTTPException(
            satus_code=500,
            detail=str(e)
        )