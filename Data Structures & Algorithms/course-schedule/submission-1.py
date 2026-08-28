class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d=defaultdict(list)
        indegree=[0]*numCourses
        order=[]
        for a,b in prerequisites:
            d[b].append(a)
            indegree[a]+=1
        
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)

        while q:
            num=q.popleft()
            order.append(num)
            for node in d[num]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        if len(order)==numCourses:
            return True
        return False