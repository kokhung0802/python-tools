import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleep for {seconds} second(s)")
    time.sleep(seconds)
    return "finish sleeping"


with concurrent.futures.ThreadPoolExecutor() as Executor:
    f1 = Executor.submit(do_something, 1)
    f2 = Executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())


finish = time.perf_counter()

print(f"Finished in {finish - start} seconds(s)")
