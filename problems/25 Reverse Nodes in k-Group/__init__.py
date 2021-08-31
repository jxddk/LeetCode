class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer = 0
        nums_length = len(nums)
        for index in range(nums_length):
            if nums[pointer] != nums[index]:
                pointer += 1
                nums[pointer] = nums[index]
            # remember that the last item also deserves a +
            if index == nums_length - 1:
                pointer += 1
        return pointer


examples = [
    (([],), 0),
    (([1, 1, 2],), 2),
    (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), 5),
]
