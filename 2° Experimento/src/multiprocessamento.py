import time
from multiprocessing import Pool, cpu_count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(is_prime, range(50000))
    count = sum(results)
    end = time.time()

    print(f"Números primos encontrados: {count}")
    print(f"Tempo (multiprocessamento): {end - start:.2f} segundos")
