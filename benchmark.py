import redis
import time
import threading
from tabulate import tabulate

# Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6380
TOTAL_OPERATIONS = 100000
CONCURRENT_CLIENTS = 50

# To store benchmark results
benchmark_results = []


# Benchmark function for a specific command
def benchmark_command(command_name, command_func, operation_count):
    start_time = time.time()
    threads = []
    operations_per_client = operation_count // CONCURRENT_CLIENTS

    def worker(client_id):
        try:
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
            for i in range(operations_per_client):
                command_func(r, client_id, i)
        except Exception as e:
            print(f"Error in client {client_id}: {e}")

    for client_id in range(CONCURRENT_CLIENTS):
        thread = threading.Thread(target=worker, args=(client_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time
    throughput = operation_count / elapsed_time
    benchmark_results.append(
        [
            command_name,
            f"{elapsed_time:.2f} seconds",
            f"{throughput:.2f} ops/sec",
            TOTAL_OPERATIONS,
            CONCURRENT_CLIENTS,
        ]
    )


# Redis command functions
def set_command(r, client_id, i):
    key = f"key_{client_id}_{i}"
    value = f"value_{i}"
    r.set(key, value)


def get_command(r, client_id, i):
    key = f"key_{client_id}_{i}"
    r.get(key)


def hset_command(r, client_id, i):
    hash_key = f"hash_{client_id}"
    field = f"field_{i}"
    value = f"value_{i}"
    r.hset(hash_key, field, value)


def hget_command(r, client_id, i):
    hash_key = f"hash_{client_id}"
    field = f"field_{i}"
    r.hget(hash_key, field)


def main():
    print("Connecting to breezedb server...")
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        r.ping()
        print("Connected to breezedb server successfully.\n")
    except redis.ConnectionError as e:
        print(f"Failed to connect to breezedb server: {e}")
        return

    print(f"Starting benchmarks with {CONCURRENT_CLIENTS} concurrent clients...\n")

    # Benchmark individual commands
    benchmark_command("SET", set_command, TOTAL_OPERATIONS)
    benchmark_command("GET", get_command, TOTAL_OPERATIONS)
    benchmark_command("HSET", hset_command, TOTAL_OPERATIONS)
    benchmark_command("HGET", hget_command, TOTAL_OPERATIONS)

    # Display results in a table
    print("\nBenchmark Results:")
    print(
        tabulate(
            benchmark_results,
            headers=[
                "Command",
                "Time Taken",
                "Throughput",
                "Total OPs",
                "Concurrent Clients",
            ],
            tablefmt="github",
        )
    )


if __name__ == "__main__":
    main()
