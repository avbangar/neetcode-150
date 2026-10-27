class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs: Dict[str, List[str]] = {}

        for string in strs:
            key = "".join(sorted(string))
            
            if key in sortedStrs:
                sortedStrs[key].append(string)
            else:
                sortedStrs[key] = [string]

        return list(sortedStrs.values())
