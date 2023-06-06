# first we create the class/template
class Rectangle:
    
    # class attributes
    width = 2
    height = 2

    # create a constructor method
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        
    def get_area(self):
        area = self.width * self.height
        return area
    
Rectangle_1 = Rectangle(5, 6)

print(Rectangle_1.get_area())