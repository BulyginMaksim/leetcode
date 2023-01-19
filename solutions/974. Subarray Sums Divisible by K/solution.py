from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixes = [0 for _ in range(k)]
        prefixes[0] = 1
        cur_sum = 0
        result = 0
        for num in nums:
            # subarray_sum + some_prefix = cur_sum -> subarray_sum = cur_sum - some_prefix
            # subarray_sum (mod k) = cur_sum - some_prefix (mod k) -> 0 = cur_sum - some_prefix (mod k)
            # some_prefix (mod k) = cur_sum (mod k)
            cur_sum += num
            result += prefixes[cur_sum % k]
            prefixes[cur_sum % k] += 1
        return result
