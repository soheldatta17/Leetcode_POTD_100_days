# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/?envType=daily-question&envId=2024-08-06

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(word)
        sorted_chars = sorted(char_count.keys(), key=lambda x: char_count[x], reverse=True)
        section = 1
        total_pushes = 0
        for i, char in enumerate(sorted_chars):
            if i != 0 and i % 8 == 0:
                section += 1
            total_pushes += char_count[char] * section
        return total_pushes
