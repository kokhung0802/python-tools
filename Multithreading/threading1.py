import threading
import time


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleep for {seconds} second(s)")
    time.sleep(seconds)
    print("finish sleeping")


t1 = threading.Thread(target=do_something, args=[1.5])
t2 = threading.Thread(target=do_something, args=[1.5])

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f"Finished in {finish - start} seconds(s)")
