import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length
    def set_width(self, width):
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    def get_diagonal(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)
    def get_picture(self):
        if self.length > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.length):
                picture += "*" * self.width + "\n"
            return picture
    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle):
            return self.get_area() / shape.get_area()
        elif isinstance(shape, Circle):
            return self.get_area() / shape.get_area()
        else:
            return "Not a shape."

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    
    