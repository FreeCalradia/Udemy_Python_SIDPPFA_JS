"""
Exercise 1:
1.)
Write a function that takes an integer number n as an input.
The function returns a list with all power of twos (2^n) from 0 to n-1.
Please use a list comprehension.

Exercise 2:
2.)
Write a function that takes the result list from 1.) as an input.
Iterate over all values of the list and print the current index and the current
value in each iteration.
"""


def exercise1(n):
    list_a = [2 ** n for n in range(0, n)]
    return list_a


def exercise2(lst):
    for idx, val in enumerate(lst):
        print(idx, val)


def main():
    n = 10
    lst = exercise1(n)
    exercise2(lst)


if __name__ == "__main__":
    main()
