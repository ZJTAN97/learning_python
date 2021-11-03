# Import the class
from cat import Cat

# Use the class
def test():
    b = Cat('KitKat', 1, 'tabby')
    c = Cat('Ohello', 1, 'brown')
    b.description()
    c.description()


if __name__ == "__main__":
    x = Cat('test')
    print(x)
    test()