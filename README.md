# Breezedb
A key value pair database built using go and [RESP](https://redis.io/docs/reference/protocol-spec/) protocol.

## Features
1. Set and get the key value.
2. Set TTL of the key, which will expire after the defined TTL.
3. Persistence using AOF(Append only file).
4. Hash map data structure support `HSET` and `HGET` commands.
5. Accept concurrent connections using go routines.

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
