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
    
    # Instance method
    def code(self):
        print(f'{self.name} is writing code..')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}')
    
    # dunder method 
    def __str__(self):
        information = f"name = {self.name}, age={self.age}, level={self.level}"
        return information

    # to compare between instance of the class
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    # cannot access the self attribute
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance of the class
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
se3 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)


se1.code()
se1.code_in_language('Python')

# To test __str__
print(se1)

# to test __eq__
print(se2 == se3)

print(se1.entry_salary(24))