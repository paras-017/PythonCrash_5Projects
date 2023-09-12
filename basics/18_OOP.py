class Employee:
    #creating constructor
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    
    def getSalary(self):
        print(f"{self.name} salary is {self.salary}")
        return "hello"

paras = Employee("Paras", 3200000)
print(paras.getSalary())