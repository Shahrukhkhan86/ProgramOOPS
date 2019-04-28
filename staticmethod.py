class Employee:
    @staticmethod

    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True
print(Employee.isopen("manday"))