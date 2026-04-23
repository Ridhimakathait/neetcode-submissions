class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap=collections.defaultdict(int)
        hmap[0]=1
        sum=0
        res=0
        for num in nums:
            sum+=num
            res+=hmap.get(sum-k,0)
            
            hmap[sum]+=1
        return res
