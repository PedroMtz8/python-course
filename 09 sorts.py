import random
import time
length = 14
# arr = [i for i in range(length, 0, -1)]
division = round(length / 2)
print(division)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{{ name: \'{self.name}\', age: {self.age} }}'
        
        # return 
    # def __str__(self):
    #     return f'{self.name} is {self.age} years old'
    
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
ages = random.choices(range(18, 80), k=100)  # Edades aleatorias entre 18 y 80
# print('LENGTH AGES', len(ages), ages, 'AGES')
# Generar 100 personas aleatorias
people = [Person(random.choice(names), age) for age in ages]

# Imprimir las personas generadas
# for person in people:
    # print(person)
    

unordered_100 = [random.randint(1, 1000) for _ in range(3000)]
# print('unordered_100', unordered_100)
print('----------------------------------------------')


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Choose the middle element as the pivot
                               # The double slash is to get the quotient integer division
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Medir el tiempo de ejecución de quick_sort
start_time1 = time.time()
result = quick_sort(unordered_100)
print('QUICK, SORT: ') # [1, 1, 2, 3, 6, 8, 10]
end_time1 = time.time()
# print('time', end_time - start_time)
print('time', (end_time1 - start_time1) * 1000)

print('----------------------------------------------')

# create a order list function withoiut quick sort method and recursive method
def order_list(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

start_time2 = time.time()
result = order_list(unordered_100)
print('ORDER LIST')
end_time2 = time.time()
# print time in milliseconds
print('time', (end_time2 - start_time2) * 1000)

print('----------------------------------------------')
