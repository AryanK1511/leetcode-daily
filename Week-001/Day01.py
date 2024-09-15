from collections import defaultdict
from typing import List

"""
You are given a string s and an integer k.
Find the length of the longest substring that contains at most k distinct characters.
"""

s = "ecebbbbaaaa"
k = 2


def func1(s: str, k: int) -> int:
    hashmap = defaultdict(int)
    left = len_substr = 0

    for right in range(len(s)):
        hashmap[s[right]] += 1

        while len(hashmap) > k:
            hashmap[s[left]] -= 1
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1

        len_substr = max(len_substr, right - left + 1)

    return len_substr


"""
# 2248: Easy
# https://leetcode.com/problems/intersection-of-multiple-arrays/description/
"""

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]


def func2(nums: List[int]) -> List[int]:
    hashmap = defaultdict(int)
    ret_arr = []

    for nums_subarr in nums:
        for num in nums_subarr:
            hashmap[num] += 1

    for k, v in hashmap.items():
        if v == len(nums):
            ret_arr.append(k)

    return sorted(ret_arr)


# print(func2(nums))

"""
# 1941: Easy
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
"""

s = "abacbc"


def func3(s: str) -> bool:
    hashmap = defaultdict(int)

    for char in s:
        hashmap[char] += 1

    return len(set(hashmap.values())) == 1


# print(func3(s))

"""
# 560: Medium
# https://leetcode.com/problems/subarray-sum-equals-k/description/
"""

nums = [1, 2, 1, 2, 1]
k = 3


def func4(nums: List[int], k: int) -> int:
    hashmap = defaultdict(int)
    hashmap[0] = 1
    count = curr = 0

    for num in nums:
        curr += num
        if curr - k in hashmap:
            count += hashmap[curr - k]
        hashmap[curr] += 1

    return count


# print(func4(nums, k))

"""
# 1248: Medium
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
"""

nums = [1, 1, 2, 1, 1]
k = 3


def func5(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


print(func5(nums, k))
