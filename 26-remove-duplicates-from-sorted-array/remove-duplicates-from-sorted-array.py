class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the index for the unique elements
        unique_index = 1
        
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it is unique
            if nums[i] != nums[i - 1]:
                # Move it to the position of unique_index and increment unique_index
                nums[unique_index] = nums[i]
                unique_index += 1
        
        return unique_index
        