"""This algorithm is used to check the primality of integers from 0 to 50000.
Beyond this interval, it gives erroneous results."""


import math


def primalite(n):
    if n < 2:
        print(n, "is not prime")
        return

    if n == 2:
        print(n, "is prime")
        return

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            print(n, "is not prime")
            return

    print(n, "is prime")


number = int(input("Enter your number : "))

primalite(number)
