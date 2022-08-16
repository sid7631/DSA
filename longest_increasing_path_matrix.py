import collections

class Solution:#329. Longest Increasing Path in a Matrix
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix:
            return 0
        self.Directions =[(0,1),(1,0),(0,-1),(-1,0)]
        m, n = len(matrix), len(matrix[0])
        #memoization visited,and record steps
        visited = collections.defaultdict(int)
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix,i,j,visited))
        return ans
        
    def dfs(self, matrix, x, y,visited):  #visited {(i,j):count}
        if (x,y) in visited:
            return visited[(x,y)]
        for dx, dy in self.Directions:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
                #dfs to search the longest increasing path(N-1), not include itself
                visited[(x,y)] = max(visited[(x,y)], self.dfs(matrix,nx,ny,visited))
        #add the square itself
        visited[(x,y)] += 1
        return visited[(x,y)]

s = Solution()
s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])