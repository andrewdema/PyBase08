'''1(1)(0), 1(2)(0), 2(3)(1), 3(4)(2), 5(5)(3), 8(6)(4), 13(7)(5), 21(8)(6), 34(9)(7), 55(10)(8), ...
Обозначим fib(n)(i), где fib - это число Фибоначчи, n - номер числа (натуральное число), i - кол-во циклов '''

CONST = 1
fib1 = CONST
fib2 = CONST
print('Calculate the element of the Fibonacci series according to the number entered.')
n = int(input('Please enter the Fibonacci number: '))
if n < 1:
    print('Enter a natural number! For example, 1, 2, 3, 4, 5, 6, 7, 8, 9 …')
elif n == 1 or n == 2:
    print ('Согласно определения первые два числа из ряда Фибоначчи равны ', CONST)
else:
    i = 2 # так как первый цикл обращается сразу к 3-му элемену (n = 3)
    while n != i: # как только номер цикла совпадет с номером элемента следует выйти из цикла i = n
        fib_sum = fib2 + fib1
        fib1 = fib2  # второй элемент превратить надо в первый
        fib2 = fib_sum  # сумма превращается во второй. И так по циклу пока счетчик не остановит цикл
        i += 1
    print('It corresponds to the element of the Fibonacci series', fib_sum)

# в блоке else начинал думать так: i = 0, и когда n=i+2 то надо остановить цикл, а потом просто додумался сделать i=2