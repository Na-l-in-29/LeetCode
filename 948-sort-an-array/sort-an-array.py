from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    
    def mergeSort(self, nums: List[int], left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)
    
    def merge(self, nums: List[int], left: int, mid: int, right: int):
        # Create temporary arrays
        n1 = mid - left + 1
        n2 = right - mid
        
        L = nums[left:mid + 1]
        R = nums[mid + 1:right + 1]
        
        # Initial indexes for subarrays and merged array
        i = 0
        j = 0
        k = left
        
        # Merge the temp arrays back into nums[left:right+1]
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of L[], if any
        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of R[], if any
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1

