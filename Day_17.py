# https://leetcode.com/problems/maximum-number-of-points-with-cost

class Solution:
    def maxPoints(self, points):
        m, n = len(points), len(points[0])
        prev_row = points[0]
        
        for r in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            left_max[0] = prev_row[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c - 1] - 1, prev_row[c])
            
            right_max[-1] = prev_row[-1]
            for c in range(n - 2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, prev_row[c])
            
            curr_row = [0] * n
            for c in range(n):
                curr_row[c] = points[r][c] + max(left_max[c], right_max[c])
            
            prev_row = curr_row
        
        return max(prev_row)
