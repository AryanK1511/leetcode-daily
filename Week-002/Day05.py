# Write a recursive program that takes a limit 'n' and then prints the numbers from n to 1
def func1(n):
    print(n)

    if n == 1:
        return

    func1(n - 1)


# Write a recursive program that takes a limit 'n' and prints the numbers from 1 to n
def func2(n):
    func2_helper(n, 1)


def func2_helper(n, count):
    print(count)

    if count == n:
        return

    func2_helper(n, count + 1)


# func2(10)


"""
# 509. Easy
# https://leetcode.com/problems/fibonacci-number/submissions/1402789551/
"""


def func3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return func3(n - 1) + func3(n - 2)


# print(func3(5))
