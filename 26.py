class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        unique = []

        while i < len(nums):
            if nums[i] in unique:
                nums.pop(i)
            else:
                unique.append(nums[i])
                i += 1

        return len(unique)
        