"""
The best approach is always to use a separate iterator class and always create a new
instance of an iterator through the __iter__ method. Each iterator instance has to
manage its own internal state.

to create an iterator, we need to implement the __iter__ and __next__
methods, manage internal state, and raise a StopIteration exception when there are
no values available.

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

    def __iter__(self):
        self._index = 1
        return WeekIterator(self.days)


class WeekIterator:
    def __init__(self, days2):
        self.days_ref = days2
        self._index = 1

    def __next__(self):

        if self._index < 1 | self._index > 8:
            raise StopIteration
        else:
            ret_value = self.days_ref[self._index]
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
