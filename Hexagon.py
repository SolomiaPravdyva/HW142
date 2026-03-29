from Polygon import Polygon

class Hexagon(Polygon):
    def __init__(self, points):
        if len(points)!=6:
            raise ValueError("Помилка: потрібно 6 точок")
        super().__init__(points)