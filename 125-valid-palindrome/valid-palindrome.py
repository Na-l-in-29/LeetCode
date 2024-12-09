class Solution:
    def isPalindrome(self, s: str) -> bool:
        conv = ""
        for l in s:
            if l.isalnum():
                conv += l
        res = conv.lower()
        return conv.lower()[::-1]  == res