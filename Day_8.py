# https://leetcode.com/problems/spiral-matrix-iii/?envType=daily-question&envId=2024-08-08

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        steps=1
        r, c = rStart, cStart
        i=0
        res=[]
        while len(res) < rows*cols:
            for x in range(2):
                dr, dc = directions[i]
                for j in range(steps):
                    if (0<=r<rows and 0<=c<cols):
                        res.append([r, c])
                    r, c = r + dr, c + dc
                i=(i+1)%4
            steps+=1
        return res   
