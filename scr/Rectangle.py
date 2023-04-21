from scr.Figure import Figure


class Rectangle(Figure):
    def __init__(self, height: int, width: int):
        super().__init__('Rectangle')
        self.height = height
        self.width = width


    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.height * self.width
