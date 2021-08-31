class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        for item in nums:
            if item != val:
                nums[pointer] = item
                pointer += 1
        return pointer
