# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

# in 20 out yes; in 70 out yes; in 90 out no.

number = int(input("Введите целое число: "))

if ((number % 10 == 0 and number % 5 == 0) or (number % 15 == 0)) and (number % 30 != 0):
    print('YES')
else: print('NO')