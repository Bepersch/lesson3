def task1():
    symb = input("Your letter: ")
    if len(symb) == 1:
        if (97 <= ord(symb) <= 122) or (65 <= ord(symb) <= 90):
            print("It's English letter!")
        else:
            print("It's other symbol!")
    else:
        print("It isn't one symbol!")


def task2():
    try:
        a = int(input("Your number: "))
    except ValueError:
        print("NotLikeThis")
    if a >= 0:
        fact = 1
        for i in range(a+1):
            if i > 1:
             fact *= i
        print("Your factorial: ", fact)
    else:
        print("Your number <0!")


def task3():
    for i in range(1, 10):
        for j in range(1, 11):
            print("%d * %d = %d" % (i, j, i * j))
        print("==================")
