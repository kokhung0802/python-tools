from threading import Lock, Thread


def inc_with_lock(lock):
    global x
    for _ in range(1000000):
        lock.acquire()
        x += 1
        lock.release()


x = 0

mylock = Lock()

t1 = Thread(target=inc_with_lock, args=(mylock,), name="Th 1")
t2 = Thread(target=inc_with_lock, args=(mylock,), name="Th 2")

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Total value of x is {x}")
