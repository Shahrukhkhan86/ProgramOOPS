class Employee:
    increament=1.5                     # Class Variable
    no_of_increment=0
    def __init__(self,name,salary):
        self.name=name                            # Instance  Variable
        self.salary=salary
        Employee.no_of_increment+=1
    def increass(self):
        self.salary=self.salary*Employee.increament

    @classmethod
    def change_increment(cls,amount):
        cls.increament = amount

print(Employee.no_of_increment)
Shahrukh=Employee('shahrukh1',12222)
print(Employee.no_of_increment)
print(Shahrukh.name)
print(Shahrukh.salary)
Shahrukh.increass()
print(Shahrukh.salary)