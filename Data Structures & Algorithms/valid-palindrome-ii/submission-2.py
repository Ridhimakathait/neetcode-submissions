class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if(s[i]!=s[j]):
                skipleft=s[i+1:j+1]
                skipright=s[i:j]
                return (skipleft==skipleft[::-1]) or (skipright==skipright[::-1])
            i+=1
            j-=1

        return True

        
