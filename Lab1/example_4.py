"""
Fibonacci  0, 1, 1, 2, 3, 5, 8, 13, 21...
"""


def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


def Slow_Henerator(n):
    print('\n*** Slow Henerator! ***')
    for i in range(n):
        print('n={}, Fn={}'.format(i, Fibonacci(i)))


def Fast_Henerator(n):
    row = [0, 1]
    print('\n*** Fast Henerator! ***\nn=0, Fn=0 \nn=1, Fn=1')
    for i in range(2, n):
        x = row[i - 1] + row[i - 2]
        print('n={}, Fn={}'.format(i, x))
        row.append(x)


def fibonUp():
    a = b = 1
    i = 0
    while True:
        i += 1
        print("F{} = ".format(i))
        yield a
        a, b = b, a+b


Slow_Henerator(31)
Fast_Henerator(34)

f = fibonUp()
print("\n*Fibonacci! Please, Press 'Enter' for get next number!")
while input() == '':
    print(f.__next__())




