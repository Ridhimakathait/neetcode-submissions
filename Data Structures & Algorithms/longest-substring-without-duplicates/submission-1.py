class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=[]
        maxlen=0

        for l in s:
            while l in visited:
                visited.pop(0)
            visited.append(l)
            maxlen=max(maxlen,len(visited))

        return maxlen


