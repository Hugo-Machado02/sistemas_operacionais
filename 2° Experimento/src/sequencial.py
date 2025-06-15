import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    return sum(1 for i in range(limit) if is_prime(i))

start = time.time()
count = count_primes(50000)
end = time.time()

print(f"Números primos encontrados: {count}")
print(f"Tempo (sequencial): {end - start:.2f} segundos")
