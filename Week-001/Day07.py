# Implementation of a stack in Python using Python lists
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

stack.append(5)

# if not stack:
# print("Stack is empty!")
# else:
# print(f"Stack is not empty, top is: {stack[-1]}")

"""
# 20. Easy
# https://leetcode.com/problems/valid-parentheses/description/
"""

s = "()[]{}"


def func1(s: str) -> bool:
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if not stack:
                return False

            prev_opening_bracket = stack.pop()

            if mapping[prev_opening_bracket] != char:
                return False

    return not stack


# print(func1(s))

"""
# 1047. Easy
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
"""

# s = "abbaca"
s = "azxxzayy"


def func2(s: str) -> str:
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


# print(func2(s))

"""
# 844. Easy
# https://leetcode.com/problems/backspace-string-compare/description/
"""

s = "y#fo##f"
t = "y#f#o##f"


def func3(s: str, t: str) -> bool:
    s_stack, t_stack = [], []

    for s_char in s:
        if s_char == "#":
            if s_stack:
                s_stack.pop()
        else:
            s_stack.append(s_char)

    for t_char in t:
        if t_char == "#":
            if t_stack:
                t_stack.pop()
        else:
            t_stack.append(t_char)

    return s_stack == t_stack


print(func3(s, t))
