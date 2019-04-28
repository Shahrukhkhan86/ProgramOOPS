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
class Programmer(Employee):
    def __init__(self,name,salary,progLan,exp):
        super().__init__(name,salary)                    # This function is used to call the last clss Function objects
        self.progLan = progLan
        self.exp = exp



khan=Programmer('shahrukh',1200,'python',3)

print(khan.exp)