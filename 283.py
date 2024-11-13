class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.remove(nums[i])
                zeros += 1
            else:
                i += 1

        for i in range(zeros):
            nums.append(0)

        return nums