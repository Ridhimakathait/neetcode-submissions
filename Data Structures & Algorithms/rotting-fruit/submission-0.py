class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh=0
        time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        
        while q and fresh:
            dim=[(0,1),(1,0),(0,-1),(-1,0)]
            for i in range(len(q)):
                r,c=q.popleft()
                for i,j in dim:
                    rn,cn=r+i,c+j
                    if 0 <= rn< m and 0 <=cn< n:
                        if grid[rn][cn]!=1:
                            continue
                        grid[rn][cn]=2
                        q.append((rn,cn))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1



        
