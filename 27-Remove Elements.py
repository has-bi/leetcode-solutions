class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Position to place next kept element
        k = 0

        # Check each number in array
        for i in range(len(nums)):
            # If current number is not the one we want to remove
            if nums[i] != val:
                # Keep it by moveing to the position k
                nums[k] = nums[i]
                # Move position for next kept number
                k += 1

        return k