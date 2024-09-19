from collections import defaultdict
from typing import List

"""
# 2260. Medium
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
"""

cards = [3, 4, 2, 3, 4, 7]
# cards = [1, 0, 5, 3]


def func1(cards: List[int]) -> int:
    d = defaultdict(int)
    min_len = float("inf")

    for idx, card in enumerate(cards):
        if card in d:
            temp_min_len = idx - d[card] + 1
            min_len = min(min_len, temp_min_len)
        d[card] = idx

    return min_len if min_len != float("inf") else -1


# print(func1(cards))

"""
# 2342. Medium
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
"""

nums = [18, 43, 36, 13, 7]
# nums = [10, 12, 19, 14]


def func2(nums: List[int]) -> int:
    d = defaultdict(int)
    max_sum = -1

    for num in nums:
        digit_sum = sum(int(digit) for digit in str(abs(num)))
        if digit_sum in d:
            max_sum = max(max_sum, num + d[digit_sum])
            if num > d[digit_sum]:
                d[digit_sum] = num
        else:
            d[digit_sum] = num

    return max_sum


# print(func2(nums))


"""
# 2352. Medium
# https://leetcode.com/problems/equal-row-and-column-pairs/description/
"""

# grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]


def func3(grid: List[List[int]]) -> int:
    d = defaultdict(int)

    for row in grid:
        d[tuple(row)] += 1

    n = len(grid)
    count = 0

    for i in range(n):
        col = []
        for j in range(n):
            element = grid[j][i]
            col.append(element)
        col = tuple(col)
        if col in d:
            count += d[col]

    return count


# print(func3(grid))
