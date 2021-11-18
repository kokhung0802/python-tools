an iterator object must implement two special methods: __iter__ and
__next__. To iterate on an object, the object has to implement at least the __iter__
method. Once the object implements the __iter__ method, we can call the object
iterable.


## Iterator

Every collection in Python is iterable by default

something is iterable if it has __iter__ special methods

something that is iterable does not necessary mean it is an iterator

an iterator can:

1. looped over (iterable)
2. return an iterable object(object that has __next__ method) from __iter__ method

print(dir(nums))

>>__iter__

print(next(nums))

>> Error: because it didnt have __next__ method

an iterator has a state where it remembers where it is during iteration

## Generator
A generator is a simple way of returning an iterator instance that can be used for iteration

generators are iterators but their __iter__ and __next__ methods created automatically

A generator function is similar to a normal function but with a yield statement instead of a return statement in it.

generator dont hold the entire result in memory, it yield 1 result at a time, waits for us to ask for the result

compared to list, generator do not have to store in memory, hence suitable for processing big dataset, faster performance time and consumes less memory
