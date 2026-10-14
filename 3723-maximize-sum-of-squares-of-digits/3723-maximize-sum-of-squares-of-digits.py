class Solution(object):
    def maxSumOfSquares(self, num, sum):
        s = ""

        if sum > 9 * num:
            return ""

        q = sum // 9
        r = sum % 9

        if q == num:
            return "9" * num

        if r:
            s += "9" * q
            s += str(r)
            s += "0" * (num - q - 1)
        else:
            s += "9" * q
            s += "0" * (num - q)

        return s