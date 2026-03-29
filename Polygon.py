class Polygon:
    def __init__(self, points):
        self.points=points
    def __str__(self):
        points_str = " ".join(f"({x}, {y})" for x, y in self.points)
        return f"{self.__class__.__name__}({points_str})"

    def is_by_one_side(self):
        n=len(self.points)
        if n<3:
            return False
        side =0
        for i in range(n):
            x1, y1 =self.points[i]
            x2, y2 = self.points[(i+1)%n]
            for j in range(n):
                if j==i or j == (i+1)%n:
                    continue
                x, y = self.points[j]
                value=(x2-x1)*(y-y1) - (y2-y1)*(x-x1)
                if value!=0:
                    if value>0:
                        current_side=1
                    else:
                        current_side= -1
                    if side==0:
                        side=current_side
                    elif side!=current_side:
                        return False
        return True
