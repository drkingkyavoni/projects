def calculate_time(f):
    from time import time

    def wrapper(*args, **kwargs):
        start_time = time()
        result = f(*args, **kwargs)
        duration = time() - start_time
        print("Function {} took {:.4f} secs".format(f.__name__, duration))
        return result

    return wrapper


@calculate_time