# Напишите программу, которая принимает на вход 5 чисел 
# и находит максимальное из них.

# in 1, 4, 8, 7, 5 out 8;
# in 78, 55, 36, 90, 2 out 90;

import random

def print_out(arg):
    print("{}".format(arg))

numbers = [random.randint(0, 100) for i in range(5)]
print_out(numbers)

max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print_out(max)


