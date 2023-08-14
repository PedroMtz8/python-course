array = [0] * 10 # <-- This creates an array with the same element inside multiplied for the number in the right
# In this example 0 array will have 10 times the number 0, so the length all will be 10
# print(array)

first3Numbers = [1,2,3]
nextNumbers = [4,5,6]

combinedNumbers = first3Numbers + nextNumbers
# print(combinedNumbers) # <-- This create a new array concatenated
                       #     so the second array will be just to the right of the first array

range = list(range(1, 11)) # <-- Creates an array of 10 elements from 1 to 10
                           # First argument is with what you want to start and second how much elements you want
print(range) # <-- This print [1,2,3,4,5,6,7,8,9,10]

chars = list("Hola mundo") # <-- This is like chars.split("") in javascript, separates all words 
print(chars)

