class Emp():
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        pass
    def display(self):
        print(f"Name->{self.name}\nSalary->{self.sal}")
class Man(Emp):
    def __init__(self,name,sal,dep):
        super().__init__(name,sal)
        self.dep=dep

        pass
    def display(self):
        super().display()
        print(f"dep->{self.dep}")
        
        
emp1=Emp("Praneeth",50)
man1=Man("Leo Das",100,"R&B")
man1.display()
