class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window,count={},{}

        for c in t:
            count[c]=1+count.get(c,0)

        have=0
        need=len(count)

        res=[-1,-1]
        reslen=float("infinity")
        l=0
        for i in range(len(s)):
            window[s[i]]=1+window.get(s[i],0)
            if s[i] in count and window[s[i]]==count[s[i]]:
                have+=1
            while have==need:
                if(i-l+1)<reslen:
                    reslen=i-l+1
                    res=[l,i]
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1]