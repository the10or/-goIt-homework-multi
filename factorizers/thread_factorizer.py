import threading
import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


res = []

lock = threading.RLock()


@timer
def thread_factorizer(*number):
    threads = []
    for num in number:
        thread = threading.Thread(target=calc, args=(num,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return res


def calc(num):
    first = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
    second = [num // i for i in first]
    with lock:
        res.append(sorted(first + second))


