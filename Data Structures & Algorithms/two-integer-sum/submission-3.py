class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={nums[0]:0}
        for i in range(1,len(nums)):
            if(target-nums[i]) in dict:
                return [dict[target-nums[i]],i]
            dict[nums[i]]=i