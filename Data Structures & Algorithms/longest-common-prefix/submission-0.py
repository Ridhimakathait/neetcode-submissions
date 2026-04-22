class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        match=0
        min_str=min(strs,key=len)
        max_possible_length=len(min_str)
        for j in range(max_possible_length):
            for i in range(len(strs)-1):
                if(strs[i][j]!=strs[i+1][j]):
                    
                    return ans;
                    break;
                else:
                    continue;
            ans+=strs[0][j]
        return ans
