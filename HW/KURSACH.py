from calc import *

calculator = {'+':add, '-':sub, '*':mul, '/':divi, '**':expon} #ссылка на функцию помещаем, не саму функцию!

while True:
    try:
        x = float(input('Enter the first number: '))
        oper = input('Enter the operation of the proposed: '+str(list(calculator.keys())))
        y = float(input('Enter the second number: '))
    except ValueError:
        print('Please enter a number!')
    else:
        break

result = None

if oper in list(calculator.keys()):
    result = calculator[oper](x,y) # calculator[oper] обращаемся к значению словаря по заданному ключу и вызываем ф-ию def

if result is not None:
    print(result)
else:
    print('None a number')

# try:
#     if result is not None:
#         print(result)
# except Exception as e:
#     print(e)