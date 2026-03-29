from Polygon import Polygon

class Pentagon(Polygon):
    def __init__(self, points):
        if len(points)!=5:
            raise ValueError("Помилка: потрібно 5 точок")
        super().__init__(points)