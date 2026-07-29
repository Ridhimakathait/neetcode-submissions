class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        l=0
        r=len(heights)-1

        while(l<r):
            h=min(heights[l],heights[r])
            w=r-l
            area=h*w
            maxarea=max(area,maxarea)
            if h==heights[l]:
                l+=1
            else:
                r-=1

        return maxarea

