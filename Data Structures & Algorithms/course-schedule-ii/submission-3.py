class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        d=defaultdict(list)
        indegree=[0 for i in range(numCourses)]
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
            for dep in d[num]:
                indegree[dep]-=1
                if indegree[dep]==0:
                    q.append(dep)
        if len(order)==numCourses:
            return order
        return []
