# Distributed Cache System

A backend system design project built with **FastAPI** and **Redis**, implementing core distributed caching concepts — cache-aside pattern, TTL expiration, and layered architecture — with structured logging for observability.

---

## What it demonstrates

| Concept              | Implementation                                                                 |
| -------------------- | ------------------------------------------------------------------------------ |
| Cache-Aside Pattern  | On cache miss, fetches from the data layer, stores in Redis, then returns      |
| TTL Expiration       | Keys stored in Redis with TTL using `SETEX`, automatically expiring stale data |
| Layered Architecture | Request flow: API → Service → Cache → Data layer                               |
| Observability        | Logging for cache hits, misses, and key operations                             |

---

## Architecture

```
Client
  │
  ▼
API Layer (FastAPI)
  │
  ▼
Service Layer (Business Logic)
  │
  ├── Redis Cache (Primary)
  │
  └── Data Layer (Fallback - in-memory dict)
```

---

## Flow

**Read (GET)**
Check Redis → HIT: return
→ MISS: fetch from DB → store in Redis with TTL → return

**Write (SET)**
Write to DB → update Redis

**Delete**
Remove from DB → remove from Redis

---

## Design decisions

**Why Cache-Aside?**
Keeps cache and database loosely coupled. Only frequently accessed data is cached, improving efficiency.

**Why Redis?**
Provides fast in-memory storage with built-in TTL support, making it ideal for caching use cases.

**Why layered architecture?**
Separates responsibilities across API, service, and data layers, improving maintainability and scalability.

---

## API reference

| Method   | Endpoint       | Description                       |
| -------- | -------------- | --------------------------------- |
| `GET`    | `/cache/{key}` | Retrieve value (404 if not found) |
| `POST`   | `/cache`       | Store key-value pair              |
| `DELETE` | `/cache/{key}` | Delete key                        |

---

## Setup

### Prerequisites

* Python 3.8+
* Redis server (WSL or Docker)

---

### 1. Install dependencies

```bash
pip install fastapi uvicorn redis
```

---

### 2. Start Redis (WSL)

```bash
redis-server
```

---

### 3. Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

### 4. Open API docs

http://127.0.0.1:8000/docs

---

## Sample logs

```
INFO - Cache MISS for key: user:1
INFO - Key user:1 stored in cache
INFO - Cache HIT for key: user:1
INFO - Key user:1 set in DB and cache
```

---

## Tech stack

* **Backend:** Python, FastAPI
* **Cache:** Redis
* **Data layer:** In-memory (dict)
* **Version control:** Git & GitHub

