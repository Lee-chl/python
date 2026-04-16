class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height;
    
    def double(self):
        self.width *=2
        self.height *= 2

rect = Rectangle(10,20)
print(rect.area())
rect.double()
print(rect.width,rect.height)