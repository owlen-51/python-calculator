#Calculater
print('Введите первое число:')
number1 = int(input())
print('Введите действие: +, -, *, /')
action = input()
print('Введите второе число:')
number2 = int(input())
a = '+'
b = '-' 
c = '*'
d = '/'
if action == a:
    print(number1 + number2) 
if action == b:
    print(number1 - number2) 
if action == c:
    print(number1 * number2)
if action == d:
    print(number1 / number2) 
