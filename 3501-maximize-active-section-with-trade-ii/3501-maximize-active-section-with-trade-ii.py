from dataclasses import dataclass
import itertools
from typing import List


@dataclass
class Group:
    start: int
    length: int


class SparseTable:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n == 0:
            self.st = []
            return

        self.st = [[0] * (self.n + 1) for _ in range(self.n.bit_length() + 1)]
        self.st[0][:self.n] = nums
        for i in range(1, self.n.bit_length() + 1):
            step = 1 << i
            half = 1 << (i - 1)
            for j in range(self.n - step + 1):
                self.st[i][j] = max(self.st[i - 1][j],
                                    self.st[i - 1][j + half])

    def query(self, l: int, r: int) -> int:
        if l > r or self.n == 0:
            return 0
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')
        zero_groups, zero_group_index = self._get_zero_groups(s)

        if not zero_groups:
            return [ones] * len(queries)

        merge_lengths = self._get_zero_merge_lengths(zero_groups)
        st = SparseTable(merge_lengths)

        def answer_for(l: int, r: int) -> int:

            best = ones

            left = (-1 if zero_group_index[l] == -1
                    else zero_groups[zero_group_index[l]].length -
                         (l - zero_groups[zero_group_index[l]].start))
            right = (-1 if zero_group_index[r] == -1
                     else r - zero_groups[zero_group_index[r]].start + 1)

            start_adj_idx, end_adj_idx = self._map_to_adjacent_indices(
                zero_group_index[l] + 1,
                zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1
            )

            if s[l] == '0' and s[r] == '0' and zero_group_index[l] + 1 == zero_group_index[r]:
                best = max(best, ones + left + right)

            elif start_adj_idx <= end_adj_idx:
                best = max(best, ones + st.query(start_adj_idx, end_adj_idx))

            if (s[l] == '0' and
                zero_group_index[l] + 1 <=
                (zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1)):
                best = max(best,
                           ones + left + zero_groups[zero_group_index[l] + 1].length)

            if s[r] == '0' and zero_group_index[l] < zero_group_index[r] - 1:
                best = max(best,
                           ones + right + zero_groups[zero_group_index[r] - 1].length)

            return best

        return [answer_for(l, r) for l, r in queries]

    def _get_zero_groups(self, s: str):
        zero_groups: List[Group] = []
        zero_group_index: List[int] = []
        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1].length += 1
                else:
                    zero_groups.append(Group(i, 1))
            zero_group_index.append(len(zero_groups) - 1)
        return zero_groups, zero_group_index

    def _get_zero_merge_lengths(self, zero_groups: List[Group]) -> List[int]:
        return [a.length + b.length for a, b in itertools.pairwise(zero_groups)]

    def _map_to_adjacent_indices(self, start_group_idx: int, end_group_idx: int):
        return start_group_idx, end_group_idx - 1