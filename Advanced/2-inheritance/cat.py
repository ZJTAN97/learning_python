# Class Inheritance

class Feline:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def setName(self, name):
        print(f'{self} setting name: {name}')
        self.name = name


# Tiger Class
class Tiger(Feline):
    # override the consturctor is a BAD IDEA.
    def __init__(self) -> None:
        # Super allows us to access the parent
        # LBYL Look before you leap
        # Super takes in the parent constructor arguments
        super().__init__('Tiga', 10) 
        print('Creating a tiger')

    
    def stalk(self):
        print(f'{self.name}: stalking')


c = Feline('kitty', 10)
c.setName('wdf kitty')


# if your super __init__ takes in default arguments, no need to put in here anymore, will error
t = Tiger()
t.stalk()
t.setName('renamed tiga')
print(t.name)