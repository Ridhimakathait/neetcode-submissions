class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta=collections.defaultdict(int)
        for src,dest in trust:
            delta[dest]+=1
            delta[src]-=1
        
        for i in range(1,len(delta)+1):
            if(delta[i]==(len(delta)-1)):
                return i
        return -1