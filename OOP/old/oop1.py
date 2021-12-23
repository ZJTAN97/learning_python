# class
class SoftwareEngineer:
    
    # class attribute
    alias = 'keyboard magician'

    # instance attributes
    def __init__(self, name, age, level, salary):
        # instance attribute is only tied to the specific instance
        # to be able to pass outside variables into the class
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance of the class
se1 = SoftwareEngineer('max', 20, 'Junior', 5000)

print(se1.name, se1.age)
print(SoftwareEngineer.alias)