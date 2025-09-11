class Student:
        def __init__(self,name ,rno,marks):
                self.name=name
                self.rno=rno
                self.marks=marks
        def display(self):
                print(f"{self.name}\n{self.rno}\n{self.marks}")
Std1=Student("Santhoshi","66E0",69)
Std2=Student("Santhosh","66E1",69)

Std1.display()