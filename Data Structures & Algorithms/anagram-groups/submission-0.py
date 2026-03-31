class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            # Sort each word to use as the grouping key
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())