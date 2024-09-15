from collections import defaultdict
from typing import List

"""
# 2225. Medium
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
"""
matches = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [4, 9],
    [10, 4],
    [10, 9],
]


def func1(matches: List[List[int]]) -> List[List[int]]:
    hashmap = defaultdict(int)

    for match in matches:
        hashmap[match[0]] += 0
        hashmap[match[1]] += 1

    return [
        sorted(k for k, v in hashmap.items() if v == 0),
        sorted(k for k, v in hashmap.items() if v == 1),
    ]


# print(func1(matches))

"""
# 1133. Easy
# https://leetcode.com/problems/largest-unique-number/description/
"""

nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]


def func2(nums: List[int]) -> int:
    hashmap = defaultdict(int)

    for num in nums:
        hashmap[num] += 1

    sorted_list = sorted([k for k, v in hashmap.items() if v == 1])
    return sorted_list[-1] if len(sorted_list) > 0 else -1


# print(func2(nums))

"""
1189. Easy
# https://leetcode.com/problems/maximum-number-of-balloons/description/
"""

text = "loonbalxballpoon"


def func3(text: str) -> int:
    return min(
        text.count("b"),
        text.count("a"),
        text.count("l") // 2,
        text.count("o") // 2,
        text.count("n"),
    )


# print(func3(text))


"""
# 49. Medium
# https://leetcode.com/problems/group-anagrams/description/
"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def func4(strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)
    for str in strs:
        hashmap["".join(sorted(str))].append(str)

    return list(hashmap.values())


# print(func4(strs))

"""
# 383. Easy
# https://leetcode.com/problems/ransom-note/description/
"""

ransomNote = "aa"
magazine = "aab"


def func5(ransomNote: str, magazine: str) -> bool:
    hashmap = defaultdict(int)
    for char in magazine:
        hashmap[char] += 1

    for char in ransomNote:
        if hashmap[char] <= 0:
            return False
        hashmap[char] -= 1

    return True


# print(func5(ransomNote, magazine))

"""
# 771. Easy
# https://leetcode.com/problems/jewels-and-stones/description/
"""

jewels = "aA"
stones = "aAAbbbb"


def func6(jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    return sum(stone in jewels_set for stone in stones)


# print(func6(jewels, stones))

"""
# 3. Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

s = "pwwkew"


def func7(s: str) -> int:
    hashmap = defaultdict(int)
    left = ans = 0

    for right, char in enumerate(s):
        hashmap[char] += 1

        while hashmap[char] > 1:
            hashmap[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


# print(func7(s))
