# Binary search using recursion

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 88


def binary_search(nums, target):
    return binary_search_helper(nums, target, 0, len(nums) - 1)


def binary_search_helper(nums, target, left, right):
    mid_idx = int(left + ((right - left) / 2))
    mid_item = nums[mid_idx]

    if left > right:
        return -1

    if mid_item > target:
        return binary_search_helper(nums, target, left, mid_idx - 1)
    elif mid_item < target:
        return binary_search_helper(nums, target, mid_idx + 1, right)
    else:
        return mid_idx


# print(binary_search(nums, target))


# Write a program to calculate the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


# print(factorial(5))


# Sum of digits using recursion
def sum_of_digits(num):
    if num == 0:
        return 0

    last_num = num % 10
    new_num = num // 10
    return last_num + sum_of_digits(new_num)


# print(sum_of_digits(13))


# Reverse a number using recursion
def reverse_num(num):
    sum = 0
    return reverse_num_helper(num, sum)


def reverse_num_helper(num, sum):
    if num == 0:
        return sum

    next_num = num // 10
    last_num = num % 10
    sum = sum * 10 + last_num

    return reverse_num_helper(next_num, sum)


# print(reverse_num(1234))

# Palindrome using recursion


def palindrome(s):
    return palindrome_helper(s, 0, len(s) - 1)


def palindrome_helper(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return palindrome_helper(s, left + 1, right - 1)


# print(palindrome("radar"))
# print(palindrome("sushi"))

# Count the number of zeroes in a number using recursion


def count_zeroes(num):
    return count_zeroes_helper(num, 0)


def count_zeroes_helper(num, count):
    if num == 0:
        return 1 if count == 0 else count

    last_digit = num % 10
    next_num = num // 10

    if last_digit == 0:
        return count_zeroes_helper(next_num, count + 1)

    return count_zeroes_helper(next_num, count)


# print(count_zeroes(3208910320))

"""
# 1342. Easy
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
"""


def func(num):
    return func_helper(num, 0)


def func_helper(num, steps):
    if num == 0:
        return steps

    if num % 2 == 0:
        return func_helper(num / 2, steps + 1)
    else:
        return func_helper(num - 1, steps + 1)


# print(func(14))
