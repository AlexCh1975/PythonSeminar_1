# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

# in 6.78 out 7; in 0.34 out 3; in 5 out no

number = float(input("Введите число: "))

if int(number) == float(number): print("NO")
else:
    number = (number - int(number)) * 10
    number = int(number)
    print(number)