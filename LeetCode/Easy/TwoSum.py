class Solution:
    def twoSum(self, nums, target):

        cache = {}
        return_list = []

        for i, item in enumerate(nums):
            if (target - item) in cache:
                return_list.append(cache[target-item])
                return_list.append(i)
            cache[item] = i
        return return_list



if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 26))