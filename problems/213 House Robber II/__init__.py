class Solution(object):
    def rob(self, nums: list[int]) -> int:
        # little edge case, easier to just give it special treatment
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # this is basically the previous problem, but calculated twice; one with the
        # first house excluded, and one with the last house excluded
        return max(
            self._calculate_rob(nums, 0, len(nums) - 2),
            self._calculate_rob(nums, 1, len(nums) - 1),
        )

    def _calculate_rob(self, nums: list[int], start_index: int, end_index: int) -> int:
        end_index = min(len(nums) - 1, end_index)
        searches = {start_index: 0}
        maximum_value = 0
        index = start_index - 1
        while index < end_index:
            index += 1
            if index not in searches:
                continue
            for new_index, new_value in [
                (index + 1, searches[index]),
                (index + 2, searches[index] + nums[index]),
            ]:
                maximum_value = max(new_value, maximum_value)
                if new_index > end_index:
                    continue
                searches[new_index] = (
                    new_value
                    if new_index not in searches
                    else max(searches[new_index], new_value)
                )
        return maximum_value


examples: list[tuple[tuple[list[int]], int]] = [
    (([1],), 1),
    (([1, 2, 3],), 3),
    (([2, 3, 2],), 3),
    (([1, 2, 3, 1],), 4),
]
