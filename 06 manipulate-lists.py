pets = ["Blacky", "Stich", "Perla", "Ron"]
print(pets[2:]) # <-- Returns an array from element 2 to the end of array
print(pets[:3]) # <-- Returns an array from element 0 to the 2 element of array
print(pets[1:3]) # <-- Returns an array from element 1 to 2 of array
# The number after the double point makes reference the stop, in the examples above won't return the 3 element

print(pets[-1]) # <-- This returns just the last element

print(pets[::2]) # <-- Returns the par index element, returns ["Blacky", "Perla"]
                 # The double point means that you want to obtain the elements (indexes) divisible by the indicated number
print(pets[::3]) # Here will have the indexes who are divisible between 3

print(pets[1::2]) # This do the same as above but indicates where you want to start doing it


numbers = list(range(21))
print('First example', numbers[1::2]) # Print odd numbers beacuse indicates start in the second element which
                                      # is 1 and since that element returns the indexes divisibles between 2
                     
numbers = list(range(1, 21))
print("Second example", numbers[::2]) # Another way to do the same as above