def cached(func):
    cach = {}

    def wrapper(*args):
        if args in cach:
            return cach[args]
        else:
            cach[args] = func(*args)
            return cach[args]
    return wrapper


def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


def my_faktarial(n):
    if n == 1:
        return 1
    else:
        return my_faktarial(n-1) * my_faktarial(n//2)


@cached
def my_cach_faktarial(n):
    if n == 1:
        return 1
    else:
        return my_cach_faktarial(n-1) * my_cach_faktarial(n//2)


@cached
def cach_fibo(n):
    if n <= 2:
        return 1
    else:
        return cach_fibo(n-2) + cach_fibo(n-1)


"""
def time_w(func):
    t0 = time.time()
    def time_work_dec(func):
        start = time.time()
        def wrapper(*args):
            t = time.time()
            res = func(*args)
            elapsed = time.time() - t

            return res

        elapsed = time.time() - start
        print(elapsed)
        return wrapper

    print("{}".format(func))
    return time_work_dec(func)
"""