class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        return self._build_list(k + 1) + [_ + 1 for _ in range(k + 1, n)]

    def _build_list(self, n: int) -> list[int]:
        # it's like Gauss and 5050; the highest number minus lowest number is always
        # a unique difference (since it's the first one); likewise, the highest number
        # minus the next lowest number is unique, as it the next highest number minus
        # the next lowest number... so in the end, just alternating high-low from 1 to n
        # gives a list with n-1 unique differences
        bottom_count = 1
        top_count = n
        result = []
        while len(result) < n:
            if len(result) % 2 == 0:
                result.append(bottom_count)
                bottom_count += 1
            else:
                result.append(top_count)
                top_count -= 1
        return result


# fmt: off
examples: list[tuple[tuple[int, int], list[int]]] = [
    ((3, 1), [1, 2, 3]),
    ((3, 2), [1, 3, 2]),
]
# fmt: on
