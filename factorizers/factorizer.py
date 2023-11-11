from multy_factorizer import multy_factorizer
from multy_pool import multy_pool_factorizer
from pool import thread_pool_factorizer
from thread_factorizer import timer, thread_factorizer


@timer
def simple_factorizer(*number):

    res = []
    for num in number:
        first = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
        second = [num // i for i in first]

        res.append(sorted(first + second))

    return res


if __name__ == "__main__":
    args = [128, 255, 99999, 10651060]
    simple_factorizer(*args)
    thread_factorizer(*args)
    thread_pool_factorizer(*args)
    multy_factorizer(*args)
    multy_pool_factorizer(*args)
    smile = r'¯\_(ツ)_/ ¯'
    print(f"{'-'*20}\nlooks like it's useless for this particular task {smile}")
