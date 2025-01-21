class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Handle empty array
        if not nums:
            return 0

        # Position where we will place the next unique element
        # Why we not start at 0? cause the first element must be unique
        position = 1

        # Start from second element
        for i in range(1, len(nums)):
            # If the current element is different from previous
            if nums[i] != nums[i-1]:
            # Place it at positions
                nums[position] = nums[i]
                position += 1

        return position


        