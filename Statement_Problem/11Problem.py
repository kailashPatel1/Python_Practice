
class Employee:
    def __init__(self,name,empid,company,sallery):
        self.name=name
        self.company=company
        self.empid=empid
        self.sallery=sallery

       
    def access(self):
        print("Name:",self.name)
        print("Company:",self.company)
        print("EmployeeID:",self.empid)
        print("sallery:",self.sallery)

s1=Employee("Ram","KP6394","TCS",75000) 
s1.access() 

 # calc.py
def add(a, b):
    return a + b






