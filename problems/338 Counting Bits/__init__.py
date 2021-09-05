class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []

        # "Can you do it without using any built-in function?" - let's try without
        # using `math.log2`, by calculating all relevant powers of 2
        log_pwrs = []
        i = 0
        while True:
            v = 2 ** i
            if v > n:
                break
            log_pwrs.append(v)
            i += 1

        for number in range(n + 1):
            count = 0
            pwr_index = 1
            while pwr_index < len(log_pwrs) + 1:
                pwr = log_pwrs[len(log_pwrs) - pwr_index]
                pwr_index += 1
                if pwr > number:
                    continue
                number -= pwr
                count += 1
            ans.append(count)
        return ans


examples: list[tuple[tuple[int], list[int]]] = [
    ((2,), [0, 1, 1]),
    ((5,), [0, 1, 1, 2, 1, 2]),
]
