class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        z = "".join([char.lower() for char in s if char.isalnum()])

        return z == z[::-1]
