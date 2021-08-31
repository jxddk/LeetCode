class Solution(object):
    def rob(self, nums: list[int]) -> int:
        # at any given house, you can either SKIP, or ROB
        # SKIP moves you to the house (index+1), but ROB steals, and moves to (index+2)
        # consider this then as a path-finding problem, aiming to maximize stolen money;
        # a BFS is appropriate here, since it allows us to stop searches that have taken
        # inferior paths at any point. only the path value, not path route, is important
        searches = {0: 0}
        maximum_value = 0
        index = -1
        while index < len(nums):
            index += 1
            if index not in searches:
                continue
            # create new subpaths for both SKIP and ROB
            for new_index, new_value in [
                (index + 1, searches[index]),
                (index + 2, searches[index] + nums[index]),
            ]:
                # update the maximum value; dead-end subpaths can still contribute
                maximum_value = max(new_value, maximum_value)
                # if the subpath's target is out of range, skip it
                if new_index >= len(nums):
                    continue
                # otherwise, create or update the subpath with the new max value
                if new_index not in searches:
                    searches[new_index] = new_value
                searches[new_index] = max(searches[new_index], new_value)
        return maximum_value


examples: list[tuple[tuple[list[int]], int]] = [
    (([1, 2, 3, 1],), 4),
    (([2, 7, 9, 3, 1],), 12),
]
