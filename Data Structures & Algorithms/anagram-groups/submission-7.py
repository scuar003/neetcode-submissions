class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            hashMap["".join((sorted(word)))].append(word)
        return list(hashMap.values())