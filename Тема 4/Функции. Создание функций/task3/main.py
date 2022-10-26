# TODO запишите здесь функцию factorial

def factorial(n):
    rezultat = 1
    for a in range(1,n+1):
        rezultat *= a

    return rezultat

print(factorial(5))

# TODO распечатать результат выполнения функции factorial от числа 5
