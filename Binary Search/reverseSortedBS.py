"""
Tags:
    -Binary Search
    
Time: O(logn)
Space: O(1)
    
Apprach:
    Option1: Similar to 
        -Binary Search Basic + slight modification in choosing side
        
Problem:
        Let's suppose that we have an array sorted in descending order and we 
        want to find index of an element e within this array.
    
"""

class Solution():
    def reverseBS(self, nums, target):
        def binarySearch(start = 0, end = len(nums)-1):
            while(start <= end):
                mid = (start + end)//2
                if nums[mid] == target:
                    return mid
                elif target<nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        return binarySearch()

if __name__=='__main__':
    sol = Solution()
    nums = [9, 6, 4, 1]; target = 4 
    print(sol.reverseBS(nums, target))
