# 19. Write a Python class Student with attributes name, age, marks.

# Write a method display() to print the details.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):   
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)
  
# Creating an object for testing
s1 = Student("Kailash", 21, 85)
s1.display()



# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def display(self):
#         print("Name:",self.name) 
#         print("RollNum :",self.rollno) 
#         print("Marks:",self.marks)
     
# s1=Student("Kailash patel",20,87)
# s1.display()








