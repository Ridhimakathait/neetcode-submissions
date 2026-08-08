class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre=defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        visited=set()
        def dfs(c):
            if c in visited:
                return False
            if pre[c]==[]:
                return True
            visited.add(c)
            for p in pre[c]:
                if not dfs(p):
                    return False
            pre[c]=[]
            visited.remove(c)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

