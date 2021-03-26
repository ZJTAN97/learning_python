# inherits, extend, override
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def work(self):
        print(f'{self.name} is working..')



class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        # Refering to parent class, overwriting the parent initializer
        super().__init__(name, age, salary)
        self.level = level
    
    def debug(self):
        print(f'{self.name} is debugging..')
    
    def work(self):
        print(f'{self.name} is coding..')


class Designer(Employee):
    
    def draw(self):
        print(f'{self.name} is drawing..')

    def work(self):
        print(f'{self.name} is designing..')


se = SoftwareEngineer("Max", 25, 5000, "Junior")
print(se.name, se.age)
se.work()
se.debug()

d = Designer("Lisa", 23, 3500)
print(d.name, d.age)
d.work()
d.draw()


# Polymorphism
employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
             SoftwareEngineer("Angie", 27, 6400, "Senior"),
             Designer("Lisa", 27, 3400)]



def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)