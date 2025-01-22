class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is empty, return 0 (always found)
        if not needle:
            return 0

        # Get lengths for easy reference
        n_len = len(needle)
        h_len = len(haystack)

        # Check each possible starting postition
        for i in range(h_len - n_len + 1):
            # If substring matches needle
            if haystack[i:i+n_len] == needle:
                return i

        # If no match found
        return -1
        