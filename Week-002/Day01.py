from collections import deque

"""
# 71. Medium
# https://leetcode.com/problems/simplify-path/description/
"""

path = "/home//foo/"
path2 = "/home/user/Documents/../Pictures"
path3 = "/../"


def func1(path: str) -> str:
    stack = []
    split_path = path.split("/")
    for sub_path in split_path:
        if sub_path == ".." and len(stack) > 0:
            stack.pop()
        elif sub_path not in [".", "", ".."]:
            stack.append(sub_path)

    return "/" + "/".join(stack)


# print(func1(path))

"""
# 1544. Easy
# https://leetcode.com/problems/make-the-string-great/description/
"""

s = "leEeetcode"
# s = "Pp"
# s = "abBAcC"


def func2(s: str) -> str:
    stack = []

    for char in s:
        if stack and (
            (char.isupper() and char.lower() == stack[-1])
            or (char.islower() and char.upper() == stack[-1])
        ):
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack) if stack else ""


# ChatGPT's solution using swapcase
def remove_adjacent_opposite_case(s: str) -> str:
    stack = []

    for char in s:
        # If stack is not empty and the top of the stack is the opposite case of current char
        if stack and stack[-1] == char.swapcase():
            stack.pop()  # Remove the top if they cancel each other
        else:
            stack.append(char)  # Add current char to stack if no cancellation

    return "".join(stack)


# print(func2(s))
# print(remove_adjacent_opposite_case(s))


"""
Queue in Python
- Mostly used to implement BFS algorithm
"""

queue = deque([1, 2, 3])
queue.append(10)
queue.appendleft(30)
queue.pop()
queue.popleft()
# print(queue[0])
# print(len(queue))
# print(queue)

"""
# 933. Easy
# https://leetcode.com/problems/number-of-recent-calls/description/
"""


class RecentCounter:
    def __init__(self):
        self.d = deque()

    def ping(self, t: int) -> int:
        while self.d and self.d[0] < t - 3000:
            self.d.popleft()

        self.d.append(t)
        return len(self.d)


"""
# 346. Easy
# https://leetcode.com/problems/moving-average-from-data-stream/description/
"""


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.d = deque()

    def next(self, val: int) -> float:
        self.d.append(val)
        while self.d and len(self.d) > self.size:
            self.d.popleft()

        avg = sum(self.d) / len(self.d)

        return avg
