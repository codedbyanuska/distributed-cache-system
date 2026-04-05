# Distributed Cache System (Redis-like)

## Overview

A distributed in-memory caching system built from scratch using Python and FastAPI.
This project simulates real-world caching systems like Redis and demonstrates core distributed system concepts.

---

## Features

* Key-Value Storage
* TTL (Time-To-Live) based expiration
* Cache-Aside Pattern
* Distributed Cache (Multiple Nodes)
* Consistent Hashing with Virtual Nodes

---

## Concepts Implemented

* Caching Strategies
* Data Partitioning
* Consistent Hashing
* Distributed Systems Design
* API Layering (FastAPI)

---

## Architecture

Client → API → Service → Cache Cluster → Database

---

## Flow

### Read (GET)

1. Check cache
2. If hit → return
3. If miss → fetch from DB
4. Update cache

### Write (SET)

1. Write to DB
2. Update cache

---

## Tech Stack

* Python
* FastAPI
* In-memory cache (simulating Redis)

---

## How to Run

```bash
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

## Future Improvements

* Redis integration
* Cache replication
* Metrics & monitoring
* Dockerization

---

## Learning Outcome

Built a distributed caching system from scratch, understanding internal working of systems like Redis.
