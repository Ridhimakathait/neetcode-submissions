class Solution:
    from collections import defaultdict
    def majorityElement(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        for num in nums:
            cnt[num]+=1
        
        k=max(cnt,key=cnt.get)
        return k