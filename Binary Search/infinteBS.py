"""
Tags:
    -Binary Search
    
Time: O(logn)
Space: O(1)
    
Apprach:
    Option1: Similar to 
        -Binary Search Basic + find the right position of end ptr
        
Problem: Suppose you have a sorted array of infinite numbers, how would you 
        search an element in the array?    
"""

class Solution():
    def infiniteBS(self, nums, target):
        
        #edge case
        if nums[-1]<target:
            return -1
        if len(nums)==1:
            if nums[0] == target:
                return 0
            return -1
        
        start = 0
        end = 1
        while(nums[end]<target):
            start = end
            end = min(len(nums)-1, end*2)
        
        def binarySearch(start, end):
            while(start <= end):
                mid = (start + end)//2
                if nums[mid] == target:
                    return mid
                elif target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return -1
        
        return binarySearch(start, end)
        
if __name__=='__main__':
    sol = Solution()
    nums = [1, 4, 5, 17, 99, 100, 444, 887]
    print(sol.infiniteBS(nums, 99))
