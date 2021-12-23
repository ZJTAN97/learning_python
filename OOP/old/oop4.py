# Encapsulation is mechanism of hiding data implementation

class SoftwareEngineer:

    def __init__(self, name, age):
        # Public attributes
        self.name = name
        self.age = age
        # Protected attributes
        self._salary = None
        self._num_bugs_solved = 0
    
    def code(self):
        self._num_bugs_solved += 1
    # getter
    def get_salary(self):
        return self._salary
    
    # setter
    def set_salary(self, base_value):
        # Check value, enforce constraints
        # if value < 1000:
        #     self._salary = 1000
        # if value > 20000:
        #     self._salary = 20000
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved > 10:
            return base_value
        if self._num_bugs_solved > 100:
            return base_value * 2
        return base_value * 3
        

se = SoftwareEngineer("Max", 25)
print(se._salary)

se.set_salary(6000)
print(se.get_salary())

for i in range(140):
    se.code()

print(se.get_salary())