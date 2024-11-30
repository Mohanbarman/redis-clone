# Breezedb
A key value pair database built using go and [RESP](https://redis.io/docs/reference/protocol-spec/) protocol.

## Features
1. Persistence using AOF(Append only file).
2. Accept concurrent TCP connections using go routines.

## Supported commands
- PING    
- GET     
- SET     
- HGET    
- HSET    
- HGETALL 
- TTL     
- PEXPIREAT

## Setup
**Using docker**
```bash
$ docker-compose up
```
**Using `go` compiler**
```bash
$ go run ./main.go
```
This will start the application on port `6380` and it can be connected using standard `redis-cli` redis client

# Benchmarks
Following benchmarks are generated using the `benchmark.py` script.

| Command   | Time Taken    | Throughput      |   Total OPs |   Concurrent Clients |
|-----------|---------------|-----------------|-------------|----------------------|
| SET       | 13.67 seconds | 7315.33 ops/sec |      100000 |                   50 |
| GET       | 10.24 seconds | 9762.50 ops/sec |      100000 |                   50 |
| HSET      | 12.39 seconds | 8073.67 ops/sec |      100000 |                   50 |
| HGET      | 13.82 seconds | 7234.92 ops/sec |      100000 |                   50 |

## Running Benchmarks
1. `pip install -r requirements.txt`
2. `python benchmark.py`

