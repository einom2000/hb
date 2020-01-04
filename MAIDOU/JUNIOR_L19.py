# Fibonacci sequence creator


def fibonacci(num):
    f1 = 1
    f2 = 1
    if num >= 3:
        print(f1)
        print(f2)
        for i in range(3, num + 1):
            fn = f1 + f2
            print(fn)
            f2, f1 = fn, f2

    else:
        print('the given number is too small!')
    pass


def main(mingzi):
    global today
    print('this is the main function!')
    print('hello ' + mingzi + '!')
    print(mingzi)
    print(today)
    today = '---------'


if __name__ == '__main__':
    today = '2019/12/07'
    main('LUCA')
    print('now we back here!!')
    print(today)
    number = input('give an integer to work:')
    fibonacci(int(number))

