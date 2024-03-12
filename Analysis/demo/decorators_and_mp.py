#!/usr/bin/python3
import multiprocessing as mp


def calculate_time(f):
    import time

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        print(
            "Function {} took {:.4f} secs".format(
                f.__name__, time.perf_counter() - start
            )
        )

        return result

    return wrapper


def count(num):
    @calculate_time
    def _count(num):
        return sum((x for x in range(num**2)))

    return _count(num)


if __name__ == "__main__":
    with mp.Pool(24) as mpp:
        print("{:,}".format(mpp.apply_async(count, (10,)).get(timeout=1)))
        print("{:,}".format(mpp.apply_async(count, (100,)).get(timeout=1)))
        print("{:,}".format(mpp.apply_async(count, (1000,)).get(timeout=1)))