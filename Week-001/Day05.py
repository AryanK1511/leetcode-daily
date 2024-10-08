from collections import defaultdict
from typing import List

"""
# 525. Medium
# https://leetcode.com/problems/contiguous-array/description/
"""

nums = [0, 1, 0]


def func1(nums: List[int]) -> int:
    zero, one = 0, 0
    res = 0

    diff_index = defaultdict(int)  # diff (count[1] - count[0]) -> index

    for i, n in enumerate(nums):
        if n == 0:
            zero += 1
        else:
            one += 1

        if one - zero not in diff_index:
            diff_index[one - zero] = i

        if one == zero:
            res = one + zero
        else:
            idx = diff_index[one - zero]
            res = max(res, i - idx)

    return res


# print(func1(nums))

"""
# 560. Medium
# https://leetcode.com/problems/subarray-sum-equals-k/description/
"""

nums = [1, 2, 3]
k = 3


def func2(nums: List[int], k: int):
    d = defaultdict(int)
    d[0] = 1
    count, curr = 0, 0

    for num in nums:
        curr += num
        if curr - k in d:
            count += d[curr - k]
        d[curr] += 1

    return count


# print(func2(nums, k))


"""
# 1248. Medium
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
"""

nums = [1, 1, 2, 1, 1]
k = 3


def func3(nums: List[int], k: int):
    d = defaultdict(int)
    d[0] = 1
    curr, count = 0, 0

    for num in nums:
        curr += num % 2
        if curr - k in d:
            count += d[curr - k]
        d[curr] += 1

    return count


# print(func3(nums))
