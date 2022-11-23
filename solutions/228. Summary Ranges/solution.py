from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        first = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx - 1] == nums[idx] - 1:
                continue
            if nums[idx - 1] == first:
                result.append(str(first))
            else:
                result.append(f'{first}->{nums[idx - 1]}')
            first = nums[idx]
        if first != nums[-1]:
            result.append(f'{first}->{nums[-1]}')
        else:
            result.append(str(first))
        return result
