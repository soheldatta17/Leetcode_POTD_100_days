# https://leetcode.com/problems/number-of-senior-citizens/?envType=daily-question&envId=2024-08-01

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[11:13]) > 60 for detail in details)
