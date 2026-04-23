class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq=collections.defaultdict(int)
        for num in nums:
            freq[num]+=1

        c=len(nums)/3
        res=[]
        for key in freq:
            if freq[key]>c:
                res.append(key)

        return res
