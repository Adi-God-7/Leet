class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        dif = [abs(i-j) for i, j in zip(nums1, nums2)]
        k = k1 + k2

        if sum(dif) <= k:
            return 0

        freq = [0] * (max(dif) + 1)

        for d in dif:
            freq[d] += 1

        for d in range(len(freq)-1, 0, -1):
            if freq[d] == 0:
                continue

            if k >= freq[d]:
                k -= freq[d]
                freq[d-1] += freq[d]
                freq[d] = 0
            else:
                freq[d] -= k
                freq[d-1] += k
                k = 0
                break

        res = 0
        for d in range(len(freq)):
            res += d * d * freq[d]

        return res