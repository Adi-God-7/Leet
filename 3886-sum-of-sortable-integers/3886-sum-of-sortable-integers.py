
from itertools import accumulate, pairwise

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        array_length = len(nums)

        descent_count = [0, *accumulate(
            current > next_value
            for current, next_value in pairwise(nums)
        )]

        prefix_maximum = list(accumulate(nums, max))
        suffix_minimum = list(accumulate(
            reversed(nums), min
        ))[::-1]

        valid_cut = [True] + [
            prefix_maximum[position - 1] <= suffix_minimum[position]
            for position in range(1, array_length)
        ]

        def is_rotatable(left, right):
            return (
                descent_count[right] - descent_count[left]
                + (nums[right] > nums[left])
            ) <= 1

        def is_sortable(block_size):
            return all(
                valid_cut[left] and is_rotatable(left, left + block_size - 1)
                for left in range(0, array_length, block_size)
            )

        divisors = [
            block_size
            for block_size in range(1, array_length + 1)
            if array_length % block_size == 0
        ]

        return sum(filter(is_sortable, divisors))