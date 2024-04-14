import random

unordered_100 = [random.randint(1, 100) for _ in range(100)]
# print('unordered_100', unordered_100)
# unordered_100_elements = [i for i in range(100, 0, -1)]

object2 = {
    'name': 'John',
    'age': 28,
}

generate_10_objects = [object2.copy() for _ in range(10)]
print('generate_10_objects', generate_10_objects)

# changeAge = [object2.update({'age': 30}) for _ in range(10)]
# changeAgeForEveryObject = [obj.update({'age': 30}) for obj in generate_10_objects]
# print('changeAge', changeAgeForEveryObject)

changeAgeForEveryObject = []
for obj in generate_10_objects:
    obj.update({'age': obj['age'] + random.randint(1, 10)})
    changeAgeForEveryObject.append(obj)

print('changeAge', changeAgeForEveryObject)

# print every element in the list
# for obj in unordered_100:
#     print(obj["age"])

whatsRange = [i for i in range(100, 0, -1)]
print('whats range', whatsRange)