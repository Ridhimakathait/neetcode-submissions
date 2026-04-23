class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hset=collections.defaultdict()
        n=len(nums)
        i=1
        while i<=n:
            if i not in nums:
                return i
            i+=1
        return i