class Solution:
    def trap(self, height: List[int]) -> int:
        l_val,r_val=0,0
        n=len(height)
        l=[0]*n
        r=[0]*n
        for i in range(n):
            j=-i-1
            l[i]=l_val
            r[j]=r_val

            l_val=max(l_val,height[i])
            r_val=max(r_val,height[j])
        
        summ=0
        for i in range(n):
            pot=min(l[i],r[i])
            summ+=max(0,pot-height[i])

        return summ

