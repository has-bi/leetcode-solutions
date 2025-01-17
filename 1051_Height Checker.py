class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Create expected array by sorting heights
        expected = sorted(heights)

        # Counter for mismatches
        mismatches = 0

        # Compare each positions
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatches += 1

        return mismatches

        