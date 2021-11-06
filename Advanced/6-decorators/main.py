"""
Decorators

Everything in python is an object
That means functions can be used as objects

A decorator takes in a function, adds some functionality and returns it.
"""


# Bad practice decorator
"""
does not return anything within the decorator function
"""
def test_decorator(func):
    print('before')
    func()
    print('after')

# f = test_decorator(do_stuff)
@test_decorator
def do_stuff():
    print('Doing stuff')




# Decorator example
"""
@makeBold is equal to
f = makeBold(printName)
f()
"""
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')
    return inner # Return the inner function


@makeBold
def printName():
    print('Docker Chan')



# Decorator with params
def numCheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Can not divide by zero.')
                return False
            return True
        print(f'{o} is not a number.')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return # return nothing if they do not pass the integer check
        return func(x, y)
        
    return inner

@numCheck
def divide(a, b):
    return a/b

divide(100, 0)
divide(100, 'cat')



"""
Decorator with unknown number of params
we want a decorator that can pass params and handle anything
we want to chain them together
*args, **kwargs
"""

def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args, **kwargs)
        print('~'*20)
    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        for x in args:
            print(f'args={x}')
        for k, v in kwargs.items():
            print(f'key={k}, value={v}')
    return inner



@outline
@list_items
def display(msg):
    print(msg)


display('hello world')

@outline
@list_items
def birthday(name = '', age =0):
    print(f'Happy Birthday {name} you are {age} years old')



birthday(name='Docker', age=13)