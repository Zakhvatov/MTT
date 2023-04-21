from scr.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side: int):
        super().__init__('Square')
        self.side = side

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2
