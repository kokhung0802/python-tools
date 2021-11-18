CPU bound task - crunching numbers using CPU
I/O bound task - not using CPU (e.g: reading and writing from file system, downloading stuff online)


why use multithreading

speed up pogram by running multiple I/O bound tasks concurrently

do not run multiple codes at the same time, run the next program while waiting for the previous program to finish

## Daemon Thread
The use of daemon threads is popular in situations
where it is not an issue if a thread dies in the middle of its execution without losing or
corrupting any data.

## Queues 

Queues are very useful in multithread applications when the information has to be exchanged between different threads safely.

Three types of queues in the Queue module:

1. FIFO: In the FIFO queue, the task added first is retrieved first.
2. LIFO: In the LIFO queue, the last task added is retrieved first.
3. Priority queue: In this queue, the entries are sorted and the entry with the lowest value is retrieved first.



