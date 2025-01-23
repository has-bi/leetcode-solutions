class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Strip trailing and leading spaces, then split into words
        words = s.strip().split()

        # Return length of last word if exists
        return len(words[-1]) if words else 0
        