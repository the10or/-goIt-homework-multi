from multiprocessing import Pool, cpu_count

from thread_factorizer import timer


def task(num):
    first = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
    second = [num // i for i in first]
    return sorted(first + second)


@timer
def multy_pool_factorizer(*numbers):
    queue = []
    with Pool(
        len(numbers) // 2,
    ) as pool:
        [queue.append(i) for i in pool.map(task, numbers)]

        return queue



