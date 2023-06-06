import time


def __cache(func):
    cache = {}
    hits = {}
    hits_time = {}
    MAX_CACHE_TIME = 300
    MAX_CACHE_HITS = 10

    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(kwargs.items()))
        if cache_key in cache and is_cache_valid(cache_key):
            hits[cache_key] += 1
            return cache[cache_key]

        result = func(*args, **kwargs)
        save_in_cache(cache_key, result)
        return result

    def save_in_cache(cache_key, result):
        cache[cache_key] = result
        hits[cache_key] = 1
        hits_time[cache_key] = time.time()

    def is_cache_valid(cache_key):
        return (time.time() - hits_time[cache_key]) < MAX_CACHE_TIME and hits[cache_key] < MAX_CACHE_HITS

    def reset_decorator():
        nonlocal cache, hits, hits_time
        cache = {}
        hits = {}
        hits_time = {}

    wrapper.reset_decorator = reset_decorator
    return wrapper


@__cache
def cached(*args, **kwargs):
    _spy()
    return len(args) + len(kwargs)


def _spy():
    pass
