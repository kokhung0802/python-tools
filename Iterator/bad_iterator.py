"""
the __iter__ and __next__
methods can be implemented in the same object class. This style of implementing an
iterator is commonly found on the internet, but it is not a recommended approach and is
considered a bad design. The reason is that when we use it in the for loop, we get back
the main object as an iterator as we implemented __iter__ and __next__ in the
same class. This can give unpredictable results
"""


class Week:
    def __init__(self):
        self.days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday",
        }
        self._index = 1

    def __iter__(self):
        self._index = 1
        return self

    def __next__(self):

        if self._index < 1 | self._index > 8:
            raise StopIteration
        else:
            ret_value = self.days[self._index]
            self._index += 1

        return ret_value


if __name__ == "__main__":
    week = Week()
    iter1 = iter(week)
    iter2 = iter(week)

    print(iter1.__next__())
    print(iter2.__next__())

    print(next(iter1))
    print(next(iter2))

"""
we are iterating on the same object using two different
iterators. The results of this main program are not as expected. This is due to a common
_index attribute shared by the two iterators.
"""
