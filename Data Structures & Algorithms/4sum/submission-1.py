class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                start=j+1
                end=n-1
                while start<end:
                    if nums[i]+nums[j]+nums[start]+nums[end]==target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        start+=1
                        end-=1
                        while start<end and nums[start]==nums[start-1]:
                            start+=1
                        while start<end and nums[end]==nums[end+1]:
                            end-=1
                    elif nums[i]+nums[j]+nums[start]+nums[end]<target:
                        start+=1
                    else:
                        end-=1
        return res