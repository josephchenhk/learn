import time
from functools import wraps
import threading

def RateLimited(maxPerSecond):
    minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.clock()
            return ret
        return rateLimitedFunction
    return decorate

def ensure_time_interval(seconds):
    """
    ensure a function will not be called within specified time interval
    """
    lock = threading.Lock()
    def decorate(func):
        last_time_called = [0.0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            lock.acquire()
            elapsed = time.clock() - last_time_called[0]
            seconds_left_to_wait = seconds - elapsed
            if seconds_left_to_wait>0:
                time.sleep(seconds_left_to_wait)
            lock.release()
            ret = func(*args, **kwargs)
            last_time_called[0] = time.clock()
            return ret
        return wrapper
    return decorate

@ensure_time_interval(seconds=2)
def print_number(num):
    print(num)

if __name__=="__main__":
    for i in range(5):
        print_number(i)