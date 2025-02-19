p1 = (1, 2)
p2 = (0, 3)
p3 = (7.1, -1)
p4 = (1, 0)
p5 = (3, 6, 9)
#a = (7,) 

points = [p1, p2, p3, p4, p5]
print(points)

points.sort()
print(points)

## sort by 2nd element
def second_element(point):
    return point[1]

points.sort(key=second_element)
print(points)

points.sort(key=lambda point: point[1]) 
print(points)


points.sort(key=lambda point: point[1]) 
print(points)

# def get_size_of_fruit(fruit):
#     return ...

fruits = ["apple", "banana", "peach"]
# fruits.sort()
# fruits.sort(key=lambda fruit: len(fruit))
# # fruits.sort(key=get_size_of_fruit)

# fruits.sort(key=lambda fruit: (len(fruit), fruit))

fruits.sort(key=lambda fruit: (len(fruit), "c" not in fruit))
print(fruits)
# bools = [True, False, True, False]
# bools.sort()
# print(bools)