# Represent point in list
point = [2, 3]

def move(p, dx, dy):
    p[0]+= dx
    p[1] += dy

print(point[0], point[1])
move(point, 1, 4)
print(point[0], point[1])


# Represent point in dictionary
point = {"x": 2, "y": 3}

def move(p, dx, dy):
    p["x"]+= dx
    p["y"] += dy

print(point["x"], point["y"])
move(point, 1, 4)
print(point["x"], point["y"])


# Represent point in class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

point = Point(2, 3)
print(point.x, point.y)
point.move(1, 4)
print(point.x, point.y)