class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        op=[[] for i in range(len(nums))]
        for i in range(len(nums)):
            op[i]=pre
            pre=pre*nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            op[i]=op[i]*post
            post=post*nums[i]
        return op