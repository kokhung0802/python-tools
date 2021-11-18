from threading import Thread


def inc():
    global x
    for _ in range(1000000):
        x += 1


x = 0

# create threads
t1 = Thread(target=inc, name="Th 1")
t2 = Thread(target=inc, name="Th 2")

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Value of X is {x}")
