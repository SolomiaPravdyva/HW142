from Polygon import Polygon
from Pentagon import Pentagon
from Hexagon import Hexagon

def read_polygons(filename):
    polygons=[]
    with open(filename, "r") as f:
        for line in f:
            parts=line.split()
            if not parts:
                continue
            name=parts[0]
            nums=list(map(float, parts[1:]))
            points=[]
            for i in range(0, len(nums), 2):
                points.append((nums[i], nums[i+1]))
            if name=="Pentagon":
                polygons.append(Pentagon(points))
            elif name=="Hexagon":
                polygons.append(Hexagon(points))
            else:
                polygons.append(Polygon(points))
    return polygons
def main():
    polygons = read_polygons("input.txt")
    print("УСІ БАГАТОКУТНИКИ:")
    for p in polygons:
        print(p)
    print("\nОПУКЛІ БАГАТОКУТНИКИ:")
    for p in polygons:
        if p.is_by_one_side():
            print(p)
if __name__ == "__main__":
    main()