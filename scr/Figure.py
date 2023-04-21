class Figure:

    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def add_area(self, figure):
        assert isinstance(figure, Figure), "Ошибка. Это не геометрическая фигура"
        return self.get_area() + figure.get_area()

# Мб стоит переписать через if с проверкой является ли figure экземпляром класса Figure.
