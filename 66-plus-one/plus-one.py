class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        l = []
        for elements in digits:
            s += str(elements)
        res = int(s) + 1
        # print(list(str(res)))
        for values in str(res):
            l.append(int(values))
        return(l)
        