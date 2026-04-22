class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=1+freq.get(num,0)

        bucket=[[] for i in range(len(nums)+1)]
        for i,val in freq.items():
            bucket[val].append(i)
        ans=[]
        for i in range(len(nums),0,-1):
            if(len(ans)==k):
                return ans
            if(bucket[i]!=[]):
                ans.extend(bucket[i])
                

        return ans
        