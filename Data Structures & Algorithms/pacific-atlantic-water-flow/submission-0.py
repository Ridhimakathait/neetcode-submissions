class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_q=deque()
        p_seen=set()

        a_q=deque()
        a_seen=set()
        m,n=len(heights),len(heights[0])

        for i in range(n):
            p_q.append((0,i))
            p_seen.add((0,i))
        for j in range(1,m):
            p_q.append((j,0))
            p_seen.add((j,0))

        for i in range(n):
            a_q.append((m-1,i))
            a_seen.add((m-1,i))
        for j in range(m-1):
            a_q.append((j,n-1))
            a_seen.add((j,n-1))  
        def get_c(seen,q):
            coords=set()
            while q:
                r,c=q.popleft()
                coords.add((r,c))
                for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    rn,cn=r+i,c+j
                    if 0<=rn<m and 0<=cn<n and heights[rn][cn]>=heights[r][c] and (rn,cn) not in seen:
                        
                        seen.add((rn,cn))
                        q.append((rn,cn))
            return coords
        p_c=get_c(p_seen,p_q)
        a_c=get_c(a_seen,a_q)

        return list(p_c.intersection(a_c))






