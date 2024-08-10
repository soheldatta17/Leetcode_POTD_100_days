# https://leetcode.com/problems/regions-cut-by-slashes/submissions/1350951875/?envType=daily-question&envId=2024-08-10

class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [1] * size

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = self.UnionFind(4 * n * n)
        
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] == ' ':
                    uf.union(root, root + 1)
                    uf.union(root + 1, root + 2)
                    uf.union(root + 2, root + 3)
                elif grid[i][j] == '/':
                    uf.union(root, root + 3)
                    uf.union(root + 1, root + 2)
                elif grid[i][j] == '\\':
                    uf.union(root, root + 1)
                    uf.union(root + 2, root + 3)
                
                if j + 1 < n:
                    uf.union(root + 1, 4 * (i * n + (j + 1)) + 3)
                if i + 1 < n:
                    uf.union(root + 2, 4 * ((i + 1) * n + j))
        
        return sum(uf.find(x) == x for x in range(4 * n * n))
