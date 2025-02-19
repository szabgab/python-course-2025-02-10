planets = ["Earth", "Mars"]
fruits = ["Apple", "Banana"]

things = planets + fruits
print(things) # ['Earth', 'Mars', 'Apple', 'Banana']

things = [planets, fruits]
print(things) # [['Earth', 'Mars'], ['Apple', 'Banana']]
print(things[0]) # ['Earth', 'Mars']
print(things[1]) # ['Apple', 'Banana']
print(things[0][0]) # Earth
