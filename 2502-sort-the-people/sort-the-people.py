class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        sorted_heights = sorted(heights) 
        while sorted_heights:
            value = sorted_heights.pop(-1)
            index = heights.index(value)  
            res.append(names[index])
            names.pop(index)
            heights.pop(index)
        return res
