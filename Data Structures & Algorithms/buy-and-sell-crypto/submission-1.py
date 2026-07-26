class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lwst=prices[0]
        maxp=0
        for curr in prices:
            maxp=max(maxp,curr-lwst)
            lwst=min(lwst,curr)
        return maxp