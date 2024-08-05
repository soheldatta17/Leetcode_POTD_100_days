# https://leetcode.com/problems/kth-distinct-string-in-an-array/?envType=daily-question&envId=2024-08-05

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=Counter(arr)
        arr=tuple(arr)
        s=0
        for i in arr:
            if d[i]==1:
                s+=1
            if s==k:
                return i
        return ""
