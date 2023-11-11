from multiprocessing import Queue, Process

from thread_factorizer import timer


def task(num, queue):
    first = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
    second = [num // i for i in first]

    queue.put(sorted(first + second))


@timer
def multy_factorizer(*numbers):
    result_queue = Queue()
    processes = []
    for num in numbers:
        process = Process(target=task, args=(num, result_queue))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    return results



