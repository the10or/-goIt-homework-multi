from concurrent.futures import ThreadPoolExecutor
from thread_factorizer import timer


def task(num):
    first = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
    second = [num // i for i in first]
    return sorted(first + second)


@timer
def thread_pool_factorizer(*numbers):
    with ThreadPoolExecutor(len(numbers)) as executor:
        return list(executor.map(task, numbers))


