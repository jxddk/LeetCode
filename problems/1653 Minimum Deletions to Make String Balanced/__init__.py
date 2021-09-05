class Solution:
    def minimumDeletions(self, s: str) -> int:
        as_to_right = s.count("a")
        bs_to_left = 0
        min_balance = float("inf")

        for index, item in enumerate(s):
            if item == "a":
                as_to_right -= 1
            min_balance = min(min_balance, as_to_right + bs_to_left)
            if item == "b":
                bs_to_left += 1

        if min_balance > len(s):
            min_balance = 0

        return min_balance


# fmt: off
examples: list[tuple[tuple[str], int]] = [
    (("aababbab",), 2),
    (("bbaaaaabb",), 2),
]
# fmt: on
