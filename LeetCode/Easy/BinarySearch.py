class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) -1

        while(left <= right):

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1

            else:
                right = middle - 1
            
        return -1



solution = Solution()
arr = [-1, 0, 3, 5, 9, 12]

print(solution.search(arr, 9))
