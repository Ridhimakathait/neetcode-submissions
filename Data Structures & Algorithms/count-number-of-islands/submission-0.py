class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        islands=0

        def bfs(i,j):
            q=collections.deque()
            visit.add((i,j))
            q.append((i,j))

            while q:
                r,c=q.popleft()
                dic=[[1,0],[0,1],[-1,0],[0,-1]]

                for d1,d2 in dic:
                    if((r+d1) in range(len(grid)) and (c+d2) in range(len(grid[0]))
                    and grid[r+d1][c+d2]=="1" and (r+d1,c+d2) not in visit):
                        q.append((r+d1,c+d2))
                        visit.add((r+d1,c+d2))
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visit:
                    bfs(i,j)
                    islands+=1
        return islands
