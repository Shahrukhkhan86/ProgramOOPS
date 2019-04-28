class Employee:
    increament=1.5                     # Class Variable
    no_of_increment=0
    def __init__(self,name,salary):
        self.name=name                            # Instance  Variable
        self.salary=salary
        Employee.no_of_increment+=1
    def increass(self):
        self.salary=self.salary*Employee.increament

    @classmethod                                         # Class method its take a argument as a class not a any object
    def change_increment(cls,amount):
        cls.increament = amount
khan=Employee('shahrukh',12000)
print(khan.salary)
Employee.change_increment(2)
khan.increass()
print(khan.salary)