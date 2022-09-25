"""
Tags:
    -Binary Search
    
Time: O(logn)
Space: O(1)
    
Apprach:
    Option1: Similar to 
        -Basic BS + slight change in finding target
        
Problem:https://www.youtube.com/watch?v=W3-KgsCVH1U&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=10&ab_channel=AdityaVerma
        https://www.geeksforgeeks.org/search-almost-sorted-array/
    
Given a sorted array arr[] of size N, some elements of array are moved to 
either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or
arr[i-1] i.e. arr[i] can only be swapped with either arr[i+1] or arr[i-1].
The task is to search for an element in this array.    
"""

class Solution():
    def almostSortedBS(self, nums, target):
        def binarySearch(start = 0, end = len(nums)-1):
            while(start <= end):
                mid = (start + end)//2
                
                for idx in range(max(0, mid-1), min(len(nums)-1, mid+1)+1):    
                    if nums[idx] == target:
                        return idx
                    
                if target<nums[mid]:
                    end = mid-1
                elif target>nums[mid]:
                    start = mid+1
            return -1
        return binarySearch()

if __name__=='__main__':
    sol = Solution()
    nums = [0, 3, 40, 20, 50, 80, 70]; target = 40
    print(sol.almostSortedBS(nums, target))
