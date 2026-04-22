class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict=defaultdict(list)
        for str in strs:
            sorted_str="".join(sorted(str))
            sorted_dict[sorted_str].append(str)

        ans=[]
        for items in sorted_dict.values():
            ans.append(items)
        return ans