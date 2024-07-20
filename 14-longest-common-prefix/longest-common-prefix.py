class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        i = 0
        while i < min(len(first),len(last)) and first[i] == last[i]:
            i += 1
        return first[:i]
        