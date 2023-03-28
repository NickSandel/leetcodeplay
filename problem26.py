class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            next = index + 1
            if nums[index] == nums[next]:
                nums.pop(index)
            index += 1
        return nums

test = [1,1,2]
solution = Solution().removeDuplicates(test)
print(solution)