class Solution(object):
    def scoreOfParentheses(self, s):
        d = 0
        c = 0

        for i in range(len(s)):
            if s[i] == '(':
                d += 1
            else:
                d -= 1

                if i > 0 and s[i - 1] == '(':
                    c += 1 << d

        return c