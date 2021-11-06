"""
The Underscore
_Single
__Double
__Before
After__ --> is literally to use python keywords to use as variable names
__Both__
"""


# Underscore for Skipping
# for _ in range(5):
#     print('hello')



# Test class
class Person:
    # Weak Private
    # python lets u change it but '_' denotes internal use only
    _name = 'No Name' # we want to use it internally 
    def setName(self, name):
        self._name = name
        print(f'Name set to: {self._name}')

    
    """
    Before (Double)
    Internal use only, avoid conflict in subclass
    if you attempt to use it outside, will have no attribute error
    """
    def __think(self):
        print('Thinking to myself.')
    
    def work(self):
        self.__think()

    
    """
    Before and After
    Internal to the class.
    """
    def __init__(self):
        print('constructor')

    
    def __call__(self):
        print('call someone.')



class Child(Person):
    # This method wont work.
    def testDouble(self):
        self.__think(self)





p = Person()
p.setName('Bryan')
print(p._name)
p.__call__()

