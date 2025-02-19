fruit = ":a:pple:"
print(fruit)
clean = fruit.replace(":", "")
print(clean)


def cleaning(txt):
    print("cleaning")
    return  txt.replace(":", "")

print(cleaning(fruit))

fruits = ['apple', 'banana:', 'peach:', 'kiwi']
print(fruits)
print()

clean_fruits = map(cleaning, fruits)
print(clean_fruits)
print()
for thing in clean_fruits:
    print(thing)
    if thing.startswith("b"):
        break
    #if "x" in thing: ## contains
    #    break
print()
clean_fruits = list(map(cleaning, fruits))
print(clean_fruits)

#together = ':'.join(fruits)
#print(together) # apple:banana:peach:kiwi

print()
clean_fruits = list(map(lambda txt: txt.replace(":", ""), fruits))
print(clean_fruits)
