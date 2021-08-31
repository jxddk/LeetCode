class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        output = []
        for i in range(len(nums)):
            output.append(nums[nums[i]])
        return output


examples: list[tuple[tuple[list[int]], list[int]]] = [
    (
        ([0, 2, 1, 5, 3, 4],),
        [0, 1, 2, 4, 5, 3],
    ),
    (
        ([5, 0, 1, 2, 3, 4],),
        [4, 5, 0, 1, 2, 3],
    ),
]
