# Напишите программу, которая будет принимать на вход число N
# и выводить числа от -N до N.

# in 5 out -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input("Введите число N: "))

i = n * -1
while i <= n:
    print(i)
    i += 1