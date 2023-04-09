from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    def wrapper(*args, **kwargs):
        global execution_time
        time1 = time.time()
        result = fn(*args, **kwargs)
        time2 = time.time()
        time3 = time2 - time1
        execution_time[fn.__name__] = time3
        return result

    return wrapper

@time_decorator
def func_add(a, b, sleep_time):
    time.sleep(sleep_time)
    print(a + b)

sleep_time = 0.1
func_add(10, 20, sleep_time)
print(execution_time['func_add'])
