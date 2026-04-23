class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap=collections.defaultdict(int)
        hmap[0]=1
        sum=0
        res=0
        for num in nums:
            sum+=num
            if (sum-k) in hmap:
                res+=hmap[sum-k]
            
            hmap[sum]+=1
        return res
