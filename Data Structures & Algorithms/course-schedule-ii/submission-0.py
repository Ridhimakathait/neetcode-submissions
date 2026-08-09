class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        visited,cycle=set(),set()
        d=defaultdict(list)
        for a,b in prerequisites:
            d[b].append(a)
        def dfs(v):
            if v in visited:
                return True
            if v in cycle:
                return False
            
            cycle.add(v)
            for pre in d[v]:
                if not dfs(pre):
                    return False
            visited.add(v)
            cycle.remove(v)
            ans.append(v)
            return True
            
        
        for i in range(numCourses):
            if(i not in visited):
                if not dfs(i):
                    return []
        return ans[::-1]