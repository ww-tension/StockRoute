# === Stage 61: Add performance timing for core list and search operations ===
# Project: StockRoute
import time, random

def benchmark_list_ops(records):
    """Simple inline timing for list append and search."""
    t0 = time.perf_counter()
    # simulate append + linear scan 1000 times
    for _ in range(1000):
        records.append({"id": random.randint(1, 9999), "qty": random.randint(1, 50)})
        total = sum(r["qty"] for r in records if r["id"] % 7 == 0)
    elapsed = time.perf_counter() - t0
    return len(records), total, elapsed

def benchmark_dict_lookup(keys):
    """Time dict-based lookup vs list scan."""
    d = {k: random.randint(1, 50) for k in keys}
    targets = [f"key_{i}" for i in range(0, len(keys), 3)]
    t0 = time.perf_counter()
    hits_list = sum(1 for k in targets if k in d)
    elapsed = time.perf_counter() - t0
    return len(d), hits_list, elapsed

if __name__ == "__main__":
    recs = []
    print("list append+scan:", benchmark_list_ops(recs))
    keys = [f"key_{i}" for i in range(200)]
    print("dict lookup:", benchmark_dict_lookup(keys))
