class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_l=sorted(nums)
        max_len=1
        temp_len=1
        if(nums==[]):
            return 0
        for i in range(len(nums)-1):
            if(sorted_l[i]==sorted_l[i+1]):
                continue
            if(abs(sorted_l[i]-sorted_l[i+1])==1):
                temp_len+=1
                max_len=max(max_len,temp_len)
            else:
                temp_len=1

        return max_len
