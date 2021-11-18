from queue import Queue
from threading import Thread
from time import sleep


class MyWorker(Thread):
    def __init__(self, name, q):
        Thread.__init__(self)
        self.name = name
        self.queue = q

    def run(self):
        while True:
            item = self.queue.get()
            sleep(1)
            try:
                print(f"{self.name}: {item}")
            finally:
                self.queue.task_done()


myqueue = Queue()
for i in range(10):
    myqueue.put(f"Task {i+1}")

for i in range(5):
    worker = MyWorker(f"Th {i+1}", myqueue)
    worker.daemon = True
    worker.start()

myqueue.join()
