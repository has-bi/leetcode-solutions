class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Define the three rows of the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3= set("zxcvbnm")

        result = []

        # Check each word
        for word in words:
            # Convert word to lowercase for case-insensitive comparison
            word_lower = word.lower()
            word_set = set(word_lower)

            # Check if all letters are in any single row
            if (word_set.issubset(row1) or
                word_set.issubset(row2) or
                word_set.issubset(row3)):
                result.append(word)

        return result

        