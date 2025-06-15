import time
from threading import Thread
from queue import Queue

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def worker(numbers, output):
    while not numbers.empty():
        n = numbers.get()
        if is_prime(n):
            output.put(1)
        numbers.task_done()

if __name__ == "__main__":
    start = time.time()
    numbers = Queue()
    output = Queue()
    for i in range(50000):
        numbers.put(i)

    threads = []
    for _ in range(8):
        t = Thread(target=worker, args=(numbers, output))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    count = 0
    while not output.empty():
        count += output.get()

    end = time.time()
    print(f"Números primos encontrados: {count}")
    print(f"Tempo (multithreading): {end - start:.2f} segundos")
