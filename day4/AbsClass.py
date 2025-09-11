from abc import ABC ,abstractmethod
class Shape(ABC):             #abstract class declaration
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,len,br):
        #super().__init__()
        self.len=len
        self.br=br
    def area(self):
        return self.len*self.br
class Circle(Shape):
    def __init__(self,rad):
        #super().__init__()
        self.rad=rad
    def area(self):
        return (3.14)*self.rad*self.rad
R=Rectangle(5,6)
C=Circle(5)
print(R.area())
print(C.area())

