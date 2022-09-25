"""
Tags:
    -BS
    -BS on ans
    
Time: O(logn-finding peak idx + logn-BS)
Space: O(1)
    
Apprach:
    Option1: Similar to 
        -BS
        -BS on descending array
        -finding bitonic peak
        
Problem: given a bitonic array(like mountain containg single peak).Apply BS
    
    
"""

class Solution():
    def bitonicBS(self, nums, target):
        def reverseBS(start, end):
            while(start <= end):
                mid = (start + end)//2
                if nums[mid] == target:
                    return mid
                elif target<nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
    
        def BS(start, end):
            while(start <= end):
                mid = (start + end)//2
                # print(mid, start, end)
                if nums[mid] == target:
                    return mid
                elif target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return -1
        
        def peakIdx():
            start = 0
            end = len(nums)
            while(start<=end):
                mid = (start + end)//2
                if (mid-1<0 or nums[mid]>nums[mid-1]) and (mid+1>=len(nums) or nums[mid]>nums[mid+1]):
                    return mid
                elif mid-1>=0 and nums[mid-1]>nums[mid]:
                    end = mid-1
                elif mid+1>=0 and nums[mid+1]>nums[mid]:
                    start = mid+1
    
        idx = peakIdx()
        print('peak idx is:', idx)
        return max(BS(0, idx-1), reverseBS(idx, len(nums)-1))


if __name__=='__main__':
    sol = Solution()
    nums = [1,3,8,12,4,2]
    print(sol.bitonicBS(nums, 4))
