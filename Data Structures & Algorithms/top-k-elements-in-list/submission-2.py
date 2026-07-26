class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}

        for i in range(len(nums)):
            freq[nums[i]]=1+freq.get(nums[i],0)

        bucket=[[] for i in range(len(nums)+1)]
        for i,val in freq.items():
            bucket[val].append(i)
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            if(len(ans)==k):
                return ans
            ans.extend(bucket[i])
        return ans

