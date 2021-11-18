def foo(a, b, c):
    print(a, b, c)

## Positional arguments
foo(1, 2, 3)

## Keyword argument (order not important)
foo(c=3, b=2, a=1)

- cannot use positional arg after keyword argument
- default variables must be at then end of function parameters

## Variable length arguments

- args: tuple (positional arguments)
- kwargs: dict (keyword argument)

def foo(a, b, c, *args, **kwargs):
    for arg in args:
        print(arg)
    
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)